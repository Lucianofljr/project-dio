menu = """
    ###Menu###

[d] Depósito
[s] Saque
[e] Extrato
[q] Saír

Selecione uma das opções acima."""

saldo = 0
saque = 0
limite = 500
deposito = 0
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é inválido.")

    elif opcao == "s":
        valor =float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_numero_saque = numero_saque > 2


        if excedeu_saldo:
            print("Você não possui saldo suficiente! digite um novo valor.")

        elif excedeu_limite:
            print("Você excedeu o limite por saque, tente novamente um valor válido!")

        elif excedeu_numero_saque:
            print("Você excedeu o número de saques diários, tente novamente no dia seguinte.")

        else:
            numero_saque += 1
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Retire o valor de R$ {valor:.2f}, abaixo!")
        
    elif opcao == "e":
        print("##########EXTRATO##########\n")
        print("não foram feitas movimentação." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}\n")
        print("###########################")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")



    


