################### DECLARANDO CONJUNTOS ###################
print("DECLARANDO CONJUNTOS")
linguagens = (
    "python",
    "js",
    "c",
    "java",
    "csharp",
)

print(len(linguagens))  # 5

################### ACESSO DADOS ###################
print("ACESSO DADOS")
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

################### ITERAR CONJUNTOS ###################
print("ITERAR CONJUNTOS")
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

################### UNION ###################
print("UNION")
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)

################### INTERSECTION ###################
print("INTERSECTION")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

################### DIFFERENCE ###################
print("DIFFERENCE")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)

################### SYMMETRIC DIFFERENCE ###################
print("SYMMETRIC DIFFERENCE")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

################### ISSUBSET ###################
print("ISSUBSET")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

################### ISSUPERSET ###################
print("ISSUPERSET")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)