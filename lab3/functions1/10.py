a1  = input().split()

def unique(a1) :
    a2 = []
    for i in a1 :
        if i not in a2 :
            a2.append(i)
    
    return a2

print(unique(a1))