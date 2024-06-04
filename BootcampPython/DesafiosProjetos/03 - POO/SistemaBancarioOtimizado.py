from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self.saldo

    @property
    def numero(self):
        return self.numero

    @property
    def agencia(self):
        return self.agencia

    @property
    def cliente(self):
        return self.cliente

    @property
    def historico(self):
        return self.historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            self.saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        return False

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("Operação falhou! O valor informado é inválido.")

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Cliente(Conta):
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)




def menu():
    menu = """

    [d]\tDepositar
    [s]\tSacar
    [nc]Nova Conta
    [lc]Listar Contas
    [nu]Novo Cliente
    [e]\tExtrato
    [p]\tPix
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def chave():
    chave = """
    [t] telefone
    [c] CPF/CNPJ
    [m] E-mail
    [q] Sair
    => """
    return input(textwrap.dedent(menu))


# def transferi_pix(saldo, extrato):
#     opcao = menu()  # Chamada corrigida para a função menu()
#     if opcao == "q":
#         return saldo, extrato
#
#     elif opcao in ["t", "c", "m"]:
#         if opcao == "t":
#             chave_pix = input("Informe a chave Pix Telefone: ")
#         elif opcao == "c":
#             chave_pix = input("Informe a chave Pix CPF/CNPJ: ")
#         elif opcao == "m":
#             chave_pix = input("Informe a chave Pix E-mail: ")
#
#         valor = float(input("Informe o valor do Pix: "))
#         excedeu_saldo = valor > saldo
#
#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente.")
#         elif valor <= 0:
#             print("Operação falhou! O valor informado é inválido.")
#         else:
#             saldo -= valor
#             extrato += f"Pix: R$ {valor:.2f}\n"
#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")
#
#     return saldo, extrato