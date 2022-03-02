a = [int(n) for n in input().split()]

def histogram(a) :
    for i in a :
        for k in range(i) :
            print('*', end = '')
        print()

histogram(a)