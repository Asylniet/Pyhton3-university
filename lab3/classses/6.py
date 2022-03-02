nums = [int(n) for n in input().split()]
for i in range(2, len(nums)): 
     nums = list(filter(lambda x: x == i or x % i and x != 1, nums))
 
print(nums)