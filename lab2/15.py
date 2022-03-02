num = {
    'ONE' : '1', 
    'TWO' : '2', 
    'THR' : '3', 
    'FOU' : '4', 
    'FIV' : '5', 
    'SIX' : '6', 
    'SEV' : '7', 
    'EIG' : '8', 
    'NIN' : '9', 
    'ZER' : '0', 
}
nums = list(num.items())
one, two = input().split('+')

def cal(one, two) :
    one = [one[i : i + 3] for i in range(0, len(one), 3)]
    two = [two[i : i + 3] for i in range(0, len(two), 3)]

    first = second = ''

    for i in range(len(one)) :
        for k in range(len(nums)) :
            if one[i] == nums[k][0] :
                first += nums[k][1]

    for i in range(len(two)) :
        for k in range(len(nums)) :
            if two[i] == nums[k][0] :
                second += nums[k][1]

    result = str(int(first) + int(second))
    final = ''

    for i in range(len(result)) :
        for k in range(len(nums)) :
            if result[i] == nums[k][1] :
                final += nums[k][0]

    return final

print(cal(one, two))

#string calculator