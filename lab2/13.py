a = input()

arr = []

while a != '0' :
    a = a.split()
    a[2], a[0] = a[0], a[2]
    arr.append(a)
    a = input()

arr.sort()

for i in range(len(arr)) :
    arr[i][0], arr[i][2] = arr[i][2], arr[i][0]

for i in arr :
    print(*i)

#date sorting