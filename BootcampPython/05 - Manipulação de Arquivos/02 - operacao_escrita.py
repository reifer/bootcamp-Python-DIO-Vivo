arquivo = open(
    r"C:\Users\reina\PycharmProjects\OT\bootcamp-Python-DIO-Vivo\BootcampPython"
    r"\Manipulação de Arquivos\teste.txt", "w",
    encoding='utf-8'
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()