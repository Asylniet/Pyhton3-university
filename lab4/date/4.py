from datetime import datetime
  
a = datetime(2004, 10, 8)
b = datetime.now()

print(f"{(b - a).total_seconds()} seconds")