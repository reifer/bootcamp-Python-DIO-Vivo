# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def plano(self):
        return self.__plano

    def fazer_chamada(self, destinatario, duracao_minutos):
        custo_chamada = self.__plano.custo_chamada(duracao_minutos)

        if self.__plano.deduzir_saldo(custo_chamada):
            saldo_restante = self.__plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

    def get_nome(self):
        return self.__nome

    def get_numero(self):
        return self.__numero

    def get_plano(self):
        return self.__plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:

# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':

# TODO: Verifique se o saldo do plano é suficiente para a chamada.

# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.

# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:


# Classe Plano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def verificar_saldo(self):
        return self.__saldo

    def custo_chamada(self, duracao_minutos):
        return duracao_minutos * 0.10

    def deduzir_saldo(self, custo_chamada):
        if self.__saldo >= custo_chamada:
            self.__saldo -= custo_chamada
            return True
        else:
            return False

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:

# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:


# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# nome = input("Digite o nome do usuário: ")
# numero = input("Digite o número do telefone: ")
# saldo_inicial = float(input("Digite o saldo inicial do plano: "))

# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# destinatario = input("Digite o nome do destinatário: ")
# duracao = int(input("Digite a duração da chamada em minutos: "))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))