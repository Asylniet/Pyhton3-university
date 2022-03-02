s = str(input())
t = str(input())

for i in range(0, len(s)) :
    if t == s[i] :
        x = i
        print(i, end = ' ')
        break

for i in range(len(s) - 1, x, -1) :
    if t == s[i] :
        print(i)
        break

#first and last uccurence in string