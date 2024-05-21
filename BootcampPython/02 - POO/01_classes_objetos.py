import self

#CLASSES E OBJETOS
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Priiim Priim")

    def parar(self):
        print("Parando a bicicleta.")
        print("Bicicleta parada.")

    def correr(self):
        print("Bike voando")

    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bike = Bicicleta("vermelha", "barra forte", 1994, 200)
bike.correr()
bike.buzinar()
bike.parar()
print(bike.cor, bike.modelo, bike.ano, bike.valor)

bike2 = Bicicleta("rosa", "Ceci", 1990, 100)
bike2.buzinar() # = Bicicleta.buzinar(bike2)
print(bike2)