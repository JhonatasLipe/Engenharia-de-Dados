menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>"""

saldo = 0
Valor_limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)
    opcao_valida = opcao.lower()

    if opcao_valida == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação Falhou: O valor informado é inválido.")

    elif opcao_valida == "s": 
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > Valor_limite_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! Valor máximo de saque excedido.")
        
        elif excedeu_saques:
            print("Operação falhou! Excedido limite de saques.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação Falhou! O valor informado é inválido.")
    
    elif opcao_valida == "e":
        print("\n*********** EXTRATO **********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("********************************")
    
    elif opcao_valida == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
            