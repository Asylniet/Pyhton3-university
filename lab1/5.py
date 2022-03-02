d ,n = input().split()
d = int(d)
n = int(n)
is_good = True

if d < 500 :
    for i in range(2, d) :
        if d % i == 0 :
            is_good = False
            break
else : 
    is_good = False

if n % 2 != 0 :
    is_good = False

if is_good :
    print("Good job!")
else :
    print("Try next time!")

#distance and archer