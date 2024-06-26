from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-07-26 09:20"
mascara_ptbr = "%d/%m/%Y %A %H:%M"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))