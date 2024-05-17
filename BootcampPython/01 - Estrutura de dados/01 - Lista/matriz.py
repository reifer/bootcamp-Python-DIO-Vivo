import random

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

tamanho_da_lista = 20  # Você pode alterar o tamanho conforme necessário

# Criando a lista com números aleatórios de 0 a 100
lista_randomica = [random.randint(0, 100) for _ in range(tamanho_da_lista)] ## lista randomica sem números
lista_randomica1 = random.sample(range(0, 100 +1), 20) ## lista randomica sem números repetidos

# Imprimindo a lista
print(lista_randomica)
print(lista_randomica1)

## [n ** 2 if n > 6 else n for n in range(10) if n % 2 == 0]
##0, 4, 16,

carros = ("gol")
print(isinstance(carros, tuple))

