from datetime import datetime, timedelta

now = datetime.now()
date = now - timedelta(5)
print(date.strftime('%d-%m-Y'))