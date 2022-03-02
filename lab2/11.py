s = input().split()

a = list()
for i in range(len(s)) :
    if s[i].isalnum() == False :
        s[i] = s[i][:-1]

    if s[i] not in a :
        a.append(s[i])

print(len(a))
a.sort()

for i in a :
    print(i)

#getting every word in alphabet order seperately