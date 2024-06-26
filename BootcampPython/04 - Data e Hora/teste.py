from datetime import datetime, timezone

# # Cria um objeto datetime "aware" com o fuso horário UTC
# datetime_aware = datetime.now(timezone.utc)
#
# print(datetime_aware)

# from datetime import datetime
#
# date_string = "2023-05-01"
# date_obj = datetime.strptime(date_string, "%Y-%d-%m")

from datetime import datetime, timedelta

d = datetime(2023, 1, 1)
new_date = d + timedelta(days=10)

print(new_date)