def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    
    if numero_saques < limite_saques:
        if (
            float(valor_saque) <= limite
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
    
    return saldo, extrato, numero_saques

def deposito(saldo, valor_deposito, extrato, /):
    
    saldo += float(valor_deposito)
    extrato += f"Houve um depósito de {float(valor_deposito)}\n"
    
    return saldo, extrato

def extr(saldo, /, extrato):
    str = "Extrato"
    print(f"{str.center(20, '#')}\n\n")
    print(f"{extrato}")
    print(f"Seu saldo atual é: R${saldo:.2f}")
    print(f"{str.center(20, '#')}\n\n")
    
def criar_usuario(nome, data, cpf, endereco, senha):
    
    usuario = {cpf: {
        "cpf": cpf,
        "nome": nome, 
        "data": data,
        "endereco": endereco,
        "senha": senha,
        }
    }
    
    return usuario

def criar_cc(usuario, nconta):
    
    if not "cc" in usuario:
        usuario["cc"] = {}
        
    usuario["cc"][nconta] = {
        "agencia": "0001",
        "nconta": nconta,
        "usuario": usuario["cpf"],
        "saldo": 0,
    },
    
    return usuario

def listar_cc(usuario):
    if "cc" in usuario:
        for contas in usuario["cc"].values():
            print(contas)
            print("##########################################")
    else:
        print("Não há nenhuma conta criada!")

menu1 = f"""
    [c] criar um usuário
    [e] entrar em um usuário
    [q] sair
"""

menu2 = f"""
    [c] criar uma conta corrente
    [l] listar contas existentes
    [e] escolha uma das contas
    [v] voltar ao menu anterior
    [q] sair
"""

menu3 = f"""
    [d] depositar
    [s] saldo
    [w] sacar
    [e] extrato
    [v] voltar ao menu anterior
    [q] sair
"""

LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500
usuarios = []
opcao = ''

while not opcao == "q":
    opcao = input(menu1)
    
    if opcao == 'c':
        nome = input(f"Informe seu nome: ")
        data = input(f"Informe sua data de nascimento: ")
        cpf = input(f"Informe seu CPF: ")
        for usuario in usuarios:
            for chave, valor in usuario.items():
                if(chave == cpf):
                    cpf = input(f"Usuário já existente, tente outro CPF: ")
        senha = input(f"Informe uma senha: ")
        endereco = ''
        endereco += input("Informe o seu logradouro: ")+", "
        endereco += input("Informe o número: ")+" - "
        endereco += input("Informe o bairro: ")+" - "
        endereco += input("Informe a cidade: ")+" - "
        uf = input("Informe a UF, apenas siglas: ")
        while not len(uf) == 2:
            uf = input("Informe a UF, apenas siglas: ")
        endereco += uf
        usuarios.append(criar_usuario(nome, data, cpf, endereco, senha))
        
    elif opcao == 'e':
        cpf = input(f"Informe seu cpf: ")
        senha = ''
        for usuario in usuarios:
            for chave, valor in usuario.items():
                if(chave == cpf):
                    senha = input(f"Informe a senha: ")
                    if (usuario[chave]["senha"] == senha):
                         
                        extrato=''
                        numero_saques = 0
                        
                        while not opcao == "v" and not opcao == "q":
                            
                            opcao = input(menu2)
                            
                            if opcao == "c":
                                numero_conta = input("Digite o número da conta: ")
                                criar_cc(usuario[chave], numero_conta)
                                print("Conta criada com sucesso!")
                            elif "cc" in usuario[chave]:
                                
                                if opcao == "l":
                                    listar_cc(usuario[chave])
                                elif opcao == "e":
                                    listar_cc(usuario[chave])
                                    escolha = input(f"Das contas listadas, digite o número da conta que deseja escolher? ")
                                    
                                    while not opcao == "v" and not opcao == "q":
                                        
                                        opcao = input(menu3)
                                        
                                        if opcao == "d":
                                            valor_deposito = input(f"Quanto deseja depositar? ")
                                            usuario["cc"][escolha]["saldo"], extrato = deposito(usuario[chave]["cc"][escolha]["saldo"], valor_deposito, extrato)

                                        elif opcao == "s":
                                            print(f'Seu saldo atual é: R${usuario[chave]["cc"][escolha]["saldo"]:.2f}')

                                        elif opcao == "w":
                                            valor_sacar = input(f"Quanto deseja sacar? ")
                                            saldo, extrato, numero_saques = sacar(saldo=usuario[chave]["cc"][escolha]["saldo"], valor_saque=valor_sacar, extrato=extrato, limite=VALOR_LIMITE_SAQUE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)

                                        elif opcao == "e":
                                            extr(usuario[chave]["cc"][escolha]["saldo"], extrato=extrato)
                                            
                                        elif opcao == "v":
                                            continue
                                        elif opcao == "q":
                                            print(f"Adeus!")
                                            break
                                
                            elif opcao == "v":
                                continue
                            elif opcao == "q":
                                print(f"Adeus!")
                                break
                            else:
                                print(f"Opção inválida!")
                                
                    else:
                        print("Senha incorreta! Abortando...")
                        break

        if senha == '':
            print(f"Usuário inexistente! Abortando...")
            break

    else:
        print(f"Opção inexistente")
