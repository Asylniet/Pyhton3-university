a = [int(n) for n in input().split()]

def detecting(a) :
    # hasNum = False
    for i in range(len(a) - 2) :
        if a[i] == 0 and a[i + 1] == 0 and a[i + 2] == 7 :
            return True
    
    # if hasNum == False :
    #     return False
        
    
print(detecting(a))