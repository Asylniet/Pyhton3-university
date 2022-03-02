n = int(input())

for i in range(0, n) :
    s = str(input())
    if '@gmail.com' in s  or '@mail.ru' in s:
        print(s.split('@')[0])

#gmail
