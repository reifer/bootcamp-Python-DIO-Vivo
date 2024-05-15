menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[p] Pix
[q] Sair

=> """

chave = """

[t] telefone
[c] CPF/CNPJ
[m] E-mail
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
chave_pix = ""

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "p":
        opcao = input(chave)
        if opcao == "t":
            chave_pix = input("Informe a chave Pix telefone: ")
            valor = float(input("Informe o valor do Pix: "))

            excedeu_saldo = valor > saldo
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Pix: R$ {valor:.2f}\n"
        elif opcao == "c":
            chave_pix = input("Informe a chave Pix CPF/CNPJ: ")
            valor = float(input("Informe o valor do Pix: "))

            excedeu_saldo = valor > saldo
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Pix: R$ {valor:.2f}\n"
        elif opcao == "m":
            chave_pix = input("Informe a chave Pix E-mail: ")
            valor = float(input("Informe o valor do Pix: "))

            excedeu_saldo = valor > saldo
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Pix: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"\nO Pix foi realizado para a chave: {chave_pix}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")