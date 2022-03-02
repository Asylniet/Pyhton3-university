from math import tan, pi


sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

area = sides * (length ** 2) / (4 * tan(pi / sides))
print(int(area))