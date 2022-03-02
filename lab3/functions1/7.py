a = [int(n) for n in input().split()]

def detecting(a) :
    hasNum = False
    for i in range(len(a) - 1) :
        if a[i] == 3 and a[i + 1] == 3 :
            return True
            break
    
    if hasNum == False :
        return False
        
    
print(detecting(a))