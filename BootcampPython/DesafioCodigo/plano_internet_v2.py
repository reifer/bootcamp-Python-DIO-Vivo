# TODO: Crie uma classe UsuarioTelefone.
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.


# TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.


# A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def plano(self):
        return self.__plano

# Entrada:
nome = input()
numero = input()
plano = input()
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)