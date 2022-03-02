n = int(input())
a = list(map(int,input().split()[:n]))

max = a[0] * a[1]
for i in range(n) :
    for j in range(n - 1) :
        if i != j and a[i] * a[j] > max:
            max = a[i] * a[j]

print(max)

#maximum product of two elements