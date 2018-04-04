from datetime import date
from datetime import datetime

today = date.today()

print(today)

print(today.strftime('%d/%m/%Y'))

date_time = datetime.now()
print(date_time.strftime('%d/%m/%Y'))
