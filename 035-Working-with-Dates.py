from datetime import date
from datetime import datetime

today = date.today()

print(today)

today_has_text = today.strftime('%d/%m/%Y')
print(today_has_text)

date_time = datetime.now()
date_time_has_text = date_time.strftime('%d/%m/%Y')
print(date_time)
