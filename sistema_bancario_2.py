import textwrap

def menu():
    menu = """
    MENU:

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Novo usuário
        [5] Nova conta
        [6] Listar contas
        [7] Sair

    => """
    return int(input(textwrap.dedent(menu)))

def observacoes():
    observacoes = """
     OBS:
         SO PODE SER FEITO APENAS 3 SAQUES DIARIOS
            COM O O LIMITE DE 500R$ APENAS!
        """
    return print(observacoes)
    
def depositar(saldo,deposito,extrato, /):
    global nova_opcao 
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R${deposito:.2f}\n"
    else:
        print("\nPor favor coloque apenas numeros positivos ou maior que 0.")
        nova_opcao = 1
        
    return saldo, extrato

def sacar(*,saque,saldo,extrato,limite,limite_saques, numero_saques):
    global nova_opcao
    if limite_saques != numero_saques:
                saque = float(input("Digite o valor a ser sacado: "))
                if saque > 0:
                    if saldo >= saque:
                        if saque <= limite:
                            saldo -= saque
                            extrato += f"Saque: R${saque:.2f}\n"
                            numero_saques += 1
                            print(f"numero saque= {numero_saques}")
                            print("\nSaque efetudado com sucesso, tenha um bom dia!")
                        else:
                            print("\nVocê pode sacar apenas num valor Maior ou Igual a 500R$.")
                            nova_opcao = 2
                    else:
                        print("\nNão é possivel sacar essa quantia, saldo muito baixo.")
                else:
                    print("\nERRO, digite novamente.")
                    nova_opcao = 2
    else:
        print("\nLimite de Saques Excedido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *,extrato):
    print("\n================== EXTRATO =============================")
    print("Não foram feitas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("==========================================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n Já existe usuario com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("Usuario cadastrado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario (somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)
    global conta_criada

    if usuario:
        print("\nConta criada com sucesso!")
        conta_criada = 1
        return { "agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    else: 
        print("\nUsuario não encontrado!")

def listar_contas(contas):
    global conta_criada
    for conta in contas:
        linha = f"""
================================================================
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
================================================================
        """
        print(textwrap.dedent(linha))
    
    if conta_criada == 0:
        print("Nenhuma conta criada no momento!")
       
def main():
    AGENCIA = "0001"

    saldo = 0.0
    saque = 0.0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    global nova_opcao 
    nova_opcao = 0
    numero_conta = 0

    global conta_criada
    conta_criada = 0

    contas = []
    usuarios = []

    while True:
        
        if nova_opcao == 0:
            opcao = menu()
        else:
            opcao = nova_opcao
            nova_opcao = 0

        if opcao == 1:
            deposito = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == 2:
            observacoes()  
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = limite,
                limite_saques = limite_saques,
                numero_saques = numero_saques,
            )
            
        elif opcao == 3:
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == 6:
            listar_contas(contas)
           
        elif opcao == 7:
            print("\nObrigado por utilizar nossos serviços.")
            break
    
        else:
            print("\nOperação invalida, Selecione novamente uma das opções desejadas.")

main()