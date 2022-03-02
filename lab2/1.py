a = [int(n) for n in input().split()]

i = 0
reach = 0
while i < len(a) and i <= reach :
    reach = max(i + a[i], reach)
    i += 1

if i == len(a) :
    print(1)
else :
    print(0)


#reaching the last point in list