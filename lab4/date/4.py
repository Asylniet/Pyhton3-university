from datetime import datetime
  
b = datetime.now()
birthday = input("What is your B'day? (in DD-MM-YYYY) ")  
a = datetime.strptime(birthday,"%d-%m-%Y")

print(f"{(b - a).total_seconds()} seconds")
