from datetime import datetime, timedelta, date

data_demissão = datetime(2023, 12, 6, 10, 37, 0)

tempo_desemprego = datetime.now() - data_demissão

print(tempo_desemprego)