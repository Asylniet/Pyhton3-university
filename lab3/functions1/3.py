head = 35
legs = 94

def count(numheads, numlegs) :
    chicken = (2 * numheads) - (numlegs / 2)
    rabbit = numheads - chicken
    print(f'rabbits - {int(rabbit)}, chickens - {int(chicken)}')


count(head, legs)