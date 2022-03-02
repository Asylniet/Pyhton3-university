n = int(input())

a = []
for i in range(n) :
    upper = lower = num = False
    x = input()
    for k in x :
        if k.isupper() :
            upper = True
        elif k.islower() :
            lower = True
        elif k.isnumeric() :
            num = True
    
    if upper == True and lower == True and num == True and x not in a:
        a.append(x)
a.sort()
print(len(a))
for i in a :
    print(i)


#good passwords