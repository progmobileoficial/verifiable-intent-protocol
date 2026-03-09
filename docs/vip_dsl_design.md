# VIP-DSL (Verifiable Intent Protocol - Domain-Specific Language)

## 1. Introdução

A VIP-DSL é uma linguagem de especificação de intenção formal projetada para o Protocolo de Intenção Verificável (VIP). Seu objetivo é fornecer uma maneira concisa, não ambígua e legível por humanos e máquinas para declarar o comportamento esperado e as restrições de segurança de um módulo de software. Ao invés de depender de descrições textuais informais, a VIP-DSL permite a criação de Declarações de Intenção Formal (DIFs) que podem ser matematicamente verificadas.

## 2. Princípios de Design

*   **Clareza e Simplicidade:** A sintaxe deve ser fácil de entender e escrever, mesmo para desenvolvedores sem experiência em verificação formal.
*   **Expressividade:** Deve ser capaz de capturar uma ampla gama de intenções e restrições de segurança comuns em software.
*   **Não Ambiguidade:** Cada declaração deve ter uma única interpretação formal.
*   **Verificabilidade:** A estrutura da DSL deve facilitar a análise por ferramentas de verificação formal.
*   **Extensibilidade:** Deve ser possível adicionar novas capacidades e tipos de intenção no futuro.

## 3. Estrutura Básica de uma DIF em VIP-DSL

Uma DIF em VIP-DSL é composta por seções que definem o módulo, suas permissões e suas restrições. A estrutura geral é a seguinte:

```
INTENT <NomeDoModulo>
  VERSION <versao>
  DESCRIPTION "<descrição concisa>"

  PERMISSIONS
    <Permissao1>;
    <Permissao2>;
    ...

  CONSTRAINTS
    <Restricao1>;
    <Restricao2>;
    ...

  ASSERTIONS
    <Assercao1>;
    <Assercao2>;
    ...
END INTENT
```

## 4. Seções da VIP-DSL

### 4.1. `INTENT <NomeDoModulo>`

Define o início da declaração de intenção e o nome único do módulo de software ao qual esta DIF se aplica.

*   **Exemplo:** `INTENT MySecurePaymentModule`

### 4.2. `VERSION <versao>`

Especifica a versão da DIF. Isso permite rastrear mudanças na intenção ao longo do tempo.

*   **Exemplo:** `VERSION 1.0.0`

### 4.3. `DESCRIPTION "<descrição concisa>"`

Uma breve descrição legível por humanos sobre o propósito geral do módulo.

*   **Exemplo:** `DESCRIPTION "Processa pagamentos de forma segura sem armazenar dados sensíveis."`

### 4.4. `PERMISSIONS`

Esta seção lista as ações e recursos que o módulo **tem permissão** para acessar ou executar. Tudo o que não estiver explicitamente permitido aqui é implicitamente negado.

**Sintaxe:** `ALLOW <recurso_ou_acao>;`

**Exemplos de Permissões:**

*   `ALLOW NETWORK_OUTBOUND_HTTPS_PORT(443);` (Permite comunicação HTTPS de saída na porta 443)
*   `ALLOW FILESYSTEM_READ_ONLY("/var/log/app.log");` (Permite apenas leitura de um arquivo específico)
*   `ALLOW CPU_COMPUTATION;` (Permite uso geral da CPU para cálculos)
*   `ALLOW MEMORY_ALLOCATION(1GB);` (Permite alocação de até 1GB de memória)
*   `ALLOW CRYPTO_HASH(SHA256);` (Permite o uso da função de hash SHA256)
*   `ALLOW DATABASE_READ_WRITE("users_table");` (Permite leitura e escrita em uma tabela específica do banco de dados)

### 4.5. `CONSTRAINTS`

Esta seção define restrições adicionais ou condições que o módulo **não deve** violar, mesmo que as permissões gerais sejam concedidas. São as "regras do que não fazer".

**Sintaxe:** `DENY <restricao>;` ou `ENSURE <condicao>;`

**Exemplos de Restrições:**

*   `DENY NETWORK_INBOUND;` (Nega qualquer conexão de rede de entrada)
*   `DENY FILESYSTEM_WRITE;` (Nega qualquer operação de escrita no sistema de arquivos)
*   `DENY DATA_EXFILTRATION_TO_EXTERNAL_IP;` (Nega envio de dados para IPs externos não autorizados)
*   `ENSURE NO_SQL_INJECTION_VULNERABILITIES;` (Garante que o código não contenha vulnerabilidades de SQL Injection)
*   `ENSURE NO_BUFFER_OVERFLOWS;` (Garante que o código não contenha vulnerabilidades de Buffer Overflow)

### 4.6. `ASSERTIONS`

Esta seção contém asserções lógicas sobre o estado do sistema ou os resultados das operações do módulo. São condições que devem ser verdadeiras após a execução de certas partes do código.

**Sintaxe:** `ON <evento_ou_funcao> ASSERT <condicao_logica>;`

**Exemplos de Asserções:**

*   `ON process_payment ASSERT balance_updated_correctly;` (Após processar pagamento, o saldo deve ser atualizado corretamente)
*   `ON encrypt_data ASSERT data_is_unreadable_without_key;` (Após criptografar dados, eles devem ser ilegíveis sem a chave)
*   `ON validate_input ASSERT input_is_sanitized;` (Após validar entrada, a entrada deve estar sanitizada)

## 5. Exemplo Completo de DIF em VIP-DSL

```
INTENT UserAuthenticationService
  VERSION 1.0.0
  DESCRIPTION "Serviço responsável por autenticar usuários e gerenciar sessões de forma segura."

  PERMISSIONS
    ALLOW NETWORK_OUTBOUND_HTTPS_PORT(443); # Para comunicação com provedor de identidade
    ALLOW DATABASE_READ_WRITE("users_table", "sessions_table");
    ALLOW CRYPTO_HASH(SHA256, PBKDF2); # Para hashing de senhas
    ALLOW MEMORY_ALLOCATION(256MB); # Limite de memória

  CONSTRAINTS
    DENY NETWORK_INBOUND;
    DENY FILESYSTEM_WRITE;
    DENY DATA_EXFILTRATION_TO_EXTERNAL_IP;
    ENSURE NO_HARDCODED_CREDENTIALS;
    ENSURE NO_WEAK_CRYPTO_ALGORITHMS;

  ASSERTIONS
    ON authenticate_user ASSERT user_session_created_securely;
    ON change_password ASSERT old_password_cannot_be_reused;
END INTENT
```
