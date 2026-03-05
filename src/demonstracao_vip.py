import hashlib
import json

# --- O QUE O PROTOCOLO VIP FAZ (SIMPLIFICADO) ---

def demonstracao_vip():
    print("--- INICIANDO DEMONSTRAÇÃO DO PROTOCOLO VIP ---")
    print("\n1. DEFINIÇÃO DA INTENÇÃO (O que queremos que o código faça)")
    # Imagina que você quer um código que apenas some dois números.
    intencao = "Somar dois números e retornar o resultado."
    regras = ["Não pode acessar a internet", "Não pode apagar arquivos"]
    
    # Criamos o "contrato" (DIF)
    contrato = {"objetivo": intencao, "regras": regras}
    print(f"Contrato criado: {intencao}")
    print(f"Regras de segurança: {regras}")

    # 2. O CÓDIGO DO PROGRAMADOR (OU DA IA)
    print("\n2. RECEBENDO O CÓDIGO DO PROGRAMADOR")
    
    # Exemplo de código HONESTO
    codigo_bom = "def somar(a, b): return a + b"
    
    # Exemplo de código MALICIOSO (Tenta roubar dados enquanto soma)
    codigo_mau = "def somar(a, b): roubar_dados(); return a + b"

    # 3. GERANDO A PROVA DE CONFIANÇA (PC)
    # No VIP, o código bom recebe um "carimbo de aprovação" (hash)
    prova_bom = hashlib.sha256((codigo_bom + str(contrato)).encode()).hexdigest()
    
    print(f"Código Bom: '{codigo_bom}'")
    print(f"Carimbo de Aprovação Gerado: {prova_bom[:10]}... (sucesso!)")

    # 4. HORA DO TESTE! (O VIP verificando o código)
    print("\n3. O VIP EM AÇÃO (Verificando a segurança)")

    def verificar(codigo_para_testar, contrato_original, carimbo_original):
        # O VIP gera um novo carimbo para o código que está tentando rodar
        novo_carimbo = hashlib.sha256((codigo_para_testar + str(contrato_original)).encode()).hexdigest()
        
        if novo_carimbo == carimbo_original:
            return "✅ SEGURO! O código faz exatamente o que prometeu."
        else:
            return "❌ PERIGO! O código foi alterado ou faz coisas que não devia."

    # Testando o código bom
    print(f"Testando código honesto: {verificar(codigo_bom, contrato, prova_bom)}")

    # Testando o código malicioso (que tenta usar o mesmo carimbo)
    print(f"Testando código malicioso: {verificar(codigo_mau, contrato, prova_bom)}")

if __name__ == "__main__":
    demonstracao_vip()
  
