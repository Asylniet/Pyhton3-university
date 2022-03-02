n = int(input())

for d in range(0, n) :
    x = int(input())
    if x <= 10 :
        print('Go to work!')
    elif x <= 25 :
        print('You are weak')
    elif x <= 45 :
        print('Okay, fine')
    elif x > 45 :
        print('Burn! Burn! Burn Young!')

