arquivo = open(
    r"C:\Users\reina\PycharmProjects\OT\bootcamp-Python-DIO-Vivo\BootcampPython"
    r"\Manipulação de Arquivos\lorem.txt",
    encoding='utf-8'
)

print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# for linha in arquivo.readlines():
#     print(linha)
# print(arquivo.readlines())

# tip
# while len(linha := arquivo.readline()):
#     print(linha)
arquivo.close()