menu = """
Escolha uma opção:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=>"""

saldo = 0
limite = 500
extrato = ""
numero_deposito = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))
    match opcao:
        case 1:
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                numero_deposito += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        case 2:
            if numero_saques >= (LIMITE_SAQUES * numero_deposito):
                print("Operação falhou! Número máximo de saques excedido.")
                continue
            
            valor = float(input("Informe o valor do saque: "))

            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif valor > limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif  0 < valor:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        case 3:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        case 0:
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")