from os import sep


def divisibleGenerator(max) :
    n = 12

    while n <= max :
        if n % 3 == 0 and n % 4 == 0:
            yield n
        n += 1

n = int(input())
nums = list(divisibleGenerator(n))
print(*nums)