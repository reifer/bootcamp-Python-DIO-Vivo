def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")


def depositar(valor):
    saldo = 500
    saldo += valor

depositar(500)
sacar(100)