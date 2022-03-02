a = []
def prime(): 
    nums = [int(n) for n in input().split()]
    for i in range(len(nums)) :
        count(nums[i])


def count(n) : 
    isPrime = True
    for i in range(2, int(n / 2 + 1)) :
        isPrime = True
        if n % i == 0 : 
            isPrime = False
            break 

    if isPrime == True :
        a.append(n)

prime()
print(a)