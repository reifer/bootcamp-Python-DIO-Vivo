############## APPEND ##############
print("APEND")
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

############## CLEAR ##############
print("CLEAR")
lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []

############## COPY ##############
print("COPY")
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

############## COUNT ##############
print("COUNT")
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

############## EXTEND ##############
print("EXTEND")
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

############## INDEX ##############
print("INDEX")
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

############## POP ##############
print("POP")
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

############## REMOVE ##############
print("REMOVE")
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

############## REVERSE ##############
print("REVERSE")
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]

############## SORT ##############
print("SORT")
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

############## LEN ##############
print("LEN")
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5

############## SORTED ##############
print("SORTED")
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]