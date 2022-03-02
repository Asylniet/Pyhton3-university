def evenGenerator(max) :
    n = 0

    while n <= max :
        yield n
        n += 2
    
n = int(input())
nums = list(evenGenerator(n))
print(*nums, sep = ", ") 