def downCounter(n) :
    while n >= 0 :
        yield n
        n -= 1

n = int(input())
nums = list(downCounter(n))
print(*nums)