saldo = 1000
saque = 200
limite = 100

#print(saldo >= saque and saque <= limite)
#print(saldo >= saque or saque <= limite)

conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) and (conta_especial and saldo >= saque)
print(exp_2)

conta_saldo_suciciente = (saldo >= saque and saque <= limite)
conta_especial_saldo_suciciente = (conta_especial and saldo >= saque)

exp_3 = conta_saldo_suciciente or conta_especial_saldo_suciciente
print(exp_3)