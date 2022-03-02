import math

r = int(input())

def volume(r) :
    v = 4 / 3 * math.pi * pow(r, 3)
    return round(v, 3)

print(volume(r))