menu = """
MENU:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

  => """

observacoes = """
 OBS:
    SO PODE SER FEITO APENAS 3 SAQUES DIARIOS
    COM O O LIMITE DE 500R$ APENAS!
"""

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
nova_opcao = 0
while True:
    
    if nova_opcao == 0:
        opcao = int(input(menu))
    else:
        opcao = nova_opcao
        nova_opcao = 0

    if opcao == 1:
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
        elif deposito <= 0:
            print("\nPor favor coloque apenas numeros positivos ou maior que 0.\n")
            nova_opcao = 1
    
    elif opcao == 2:
        print(observacoes)  
        if limite_saques != numero_saques:
            saque = float(input("Digite o valor a ser sacado: "))
            if saque > 0:
                if saldo >= saque:
                    if saque <= limite:
                        saldo -= saque
                        extrato += f"Saque: R${saque:.2f}\n"
                        numero_saques = numero_saques +1
                        print("\nSaque efetudado com sucesso, tenha um bom dia!")
                    else:
                        print("\nVocê pode sacar apenas num valor Maior ou Igual a 500R$.\n")
                        nova_opcao = 2
                else:
                    print("\nNão é possivel sacar essa quantia, saldo muito baixo.\n")
            else:
                print("\nERRO, digite novamente.\n")
                nova_opcao = 2
        else:
                print("\nLimite de Saques Excedido.")


    elif opcao == 3:
        print("\n================== EXTRATO =============================")
        print("Não foram feitas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==========================================================")

    
    elif opcao == 4:
        print("\nObrigado por utilizar nossos serviços.")
        break

        
    else:
        print("\nOperação invalida, Selecione novamente uma das opções desejadas.")
