import math

def myFunc(e):
  return e[1]

a = [int(n) for n in input().split()]

x = int(input())
arr = []
for i in range(x) :
    b = [[int(n) for n in input().split()], i]
    arr.append(b)

for i in range(len(arr)) :
    s = math.sqrt((pow(arr[i][0][0] - a[0], 2)) + pow(arr[i][0][1] - a[1], 2))
    arr[i][1] = s

arr.sort(key = myFunc)

for i in range(len(arr)) :
    print(f'{arr[i][0][0]} {arr[i][0][1]}')

#closest point ordering