a = []
arr = 1
while arr != 0 :
    arr = int(input())
    if arr == 0 :
        break
    else :
        a.append(arr)

for i in range(int(len(a) / 2)) :
    print(a[i] + a[len(a) - i - 1], end = ' ')

if len(a) % 2 != 0 :
    print(a[int(len(a) / 2)])

#we get stronger