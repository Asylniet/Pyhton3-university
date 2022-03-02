n = int(input())
arr = dict()
sum = 0

for i in range(n) :
    key, value = input().split()
    if key in arr :
        arr[key] += int(value)
    else :
        arr[key] = int(value)

a = sorted(arr.items())
money = a[0][1]

for i in range(len(a)) :
    if a[i][1] > money : 
        money = a[i][1]

for i in range(len(a)) :
    if a[i][1] == money :
        print(f'{a[i][0]} is lucky!')
    else :
        print(f'{a[i][0]} has to receive {money - a[i][1]} tenge')

#compensations