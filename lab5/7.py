import re
pattern = '([a-z]+)'
results = re.findall(pattern, input())
for i in results :
    print(i.capitalize(), end = "")