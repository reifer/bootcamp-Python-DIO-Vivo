nome = "Reinaldo Junior"
idade = 44
profissao = "Desenvolvedor"
linguagem = "Python"
saldo = 17457.265670

dados = {"nome": "Reinaldo", "idade": 44}

print("Nome: %s Idade: %d" %(nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade,nome))

print("Nome: {1} Idade: {0} Nome: {1}".format(idade,nome))

print("Nome: {name} Idade: {age}".format(age = idade, name = nome))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
