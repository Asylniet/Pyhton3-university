n = int(input())
s = []
result = []
for i in range(n) :
    a = input().split()
    if a[0] == '1' :
        s.append(a)
    elif a[0] == '2' :
        result.append(s[0][1])
        s.pop(0)

for i in range(len(result)) :
    print(result[i], end = ' ')


#discs from the shelf