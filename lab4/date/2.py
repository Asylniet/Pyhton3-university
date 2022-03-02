from datetime import datetime, timedelta

now = datetime.now()

yesterday = now - timedelta(1)
print(yesterday.strftime('Yesterday - %d-%m-%Y'))

print(now.strftime("Today - %d-%m-%Y"))

tomorrow = now + timedelta(1)
print(tomorrow.strftime('Tomorrow - %d-%m-%Y'))