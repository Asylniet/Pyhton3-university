num = input().split()
if len(num) == 1 :
    r = input()
    num.append(r)

n = int(num[0])
x = int(num[1])

arr = []
for i in range(n):
    a = x + 2 * i
    arr.append(a)
    sum = arr[0]

for i in range (1, n):
    sum ^= arr[i]

print(sum)

#XOR of array