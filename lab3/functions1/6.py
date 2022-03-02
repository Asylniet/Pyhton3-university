s = input().split()

def reversing(s) :
    s.reverse()
    for i in range(len(s)) :
        print(s[i], end = ' ')
    
reversing(s)