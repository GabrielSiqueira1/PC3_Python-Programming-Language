menu = f"""
    [d] depositar
    [s] saldo
    [w] sacar
    [e] extrato
    [q] encerrar
"""

LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500
numero_saques = 0
saldo = 0
extrato = ""
opcao = ""

while not opcao == "q":
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = input(f"Quanto deseja depositar? ")
        saldo += float(valor_deposito)
        extrato = f"Houve um depósito de {float(valor_deposito)}".join(extrato)

    elif opcao == "s":
        print(f"Seu saldo atual é: R${saldo:.2f}")

    elif opcao == "w":
        if numero_saques < LIMITE_SAQUE:
            valor_saque = input(f"Quanto deseja sacar? ")
            if (
                float(valor_saque) <= 500
                and float(valor_saque) <= saldo
                and float(valor_saque) >= 0
            ):
                saldo -= float(valor_saque)
                numero_saques += 1
                extrato += f"Houve um saque de {float(valor_saque)}\n"
            else:
                print(f"Valor desejado inviável de ser sacado.")
        else:
            print(f"Excedeu o limite de saques!")

    elif opcao == "e":
        str = "Extrato"
        print(f"{str.center(20, '#')}\n")
        print(f"{extrato}")
        print(f"Seu saldo atual é: R${saldo:.2f}")
        print(f"{str.center(20, '#')}\n")

    elif opcao == "q":
        print(f"Adeus!")
        break

    else:
        print(f"Opção inexistente")
