def bin(bstring) :
    if not bstring :
        return 0
    # return (bnumb % 10 + 2 * bin(bnumb // 10))
    return bin(bstring[:-1]) * 2 + int(bstring[-1])
    
n = str(input())
print(bin(n))

# c = input()
# print(int(c, 2))