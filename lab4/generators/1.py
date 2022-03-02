def squareGenerator(max) :
    n = 1

    while n <= max :
        yield pow(n, 2)
        n += 1
    
max = int(input())
num = squareGenerator(max)
for i in num :
    print(i)