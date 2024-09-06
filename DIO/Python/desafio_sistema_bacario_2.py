def saque(*, saldo, valor, extrato, limite, numero_saques, numero_deposito, LIMITE_SAQUES):
    if numero_saques >= (LIMITE_SAQUES * numero_deposito):
        print("Operação falhou! Número máximo de saques excedido.")
        return 1
            
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return 2

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return 3
    elif  0 < valor:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques        
    else:
        print("Operação falhou! O valor informado é inválido.")
    
def deposito(saldo,valor,extrato,numero_deposito):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:            
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        numero_deposito += 1
        return saldo, extrato, numero_deposito
    else:            
        print("Operação falhou! O valor informado é inválido.")
        

def extrato(saldo,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(lista_usuarios: list):
    usuario = { nome: input("informe o nome do usuário: "),
                data_nascimento: input("informe a data de nascimento do usuário: "),
                cpf: input("informe o CPF do usuário: "),
                endereco: input("informe o endereço do usuário(logradour - bairro - cidade/estado): ")}    
    if usuario.cpf not in lista_usuarios:
        lista_usuarios.append(usuario)
        print("Conta criada com sucesso!")
        return lista_usuarios
    else:
        print("Operação falhou! O cpf ja consta no cadastro.")

def criar_conta(lista_contas: list,lista_usuario:list, contador_contas: int):
   
    if conta.numero_conta not in lista_contas:
        lista_contas.append(conta)
        print("Conta criada com sucesso!")
        return lista_contas
    else:
        print("Operação falhou! O número da conta ja consta no cadastro.")

def listar_contas(lista_contas: list):
    print(lista_contas)

def main(): 
    menu = """
    Escolha uma opção:
    [1] Novo usuário
    [2] Nova conta
    [3] Listar contas
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [0] Sair
    =>"""
    lista_contas = []
    lista_usuarios = []
    contador_contas = 1
    saldo = 0
    limite = 500
    extrato = ""
    numero_deposito = 0
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = int(input(menu))
        match opcao:
            case  1:
                criar_usuario(lista_usuarios)

            case  2:
                 conta = {numero_conta: input("informe o número da conta: "),
                        agencia: input("informe a agência da conta: "),
                        cpf: input("informe o CPF do usuário: "),
                        saldo: 0,
                        limite: 500,
                        extrato: "",
                        numero_deposito: 0,
                        numero_saques: 0,
                        LIMITE_SAQUES: 3}
                criar_conta(lista_contas,lista_usuarios,contador_contas)

            case  3:
                listar_contas(lista_contas)

            case  4:
                deposito(saldo,valor,extrato,numero_deposito)
        
            case  5:
                saque(saldo,valor,extrato,limite,numero_saques,numero_deposito,LIMITE_SAQUES)

            case  6:
                extrato(saldo,extrato)    

            case  0:
                break

            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")