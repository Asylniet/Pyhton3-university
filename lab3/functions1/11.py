s = input()

def palindrome(s) :
    isPalindrome = True
    for i in range(int(len(s) / 2)) :
        if s[i] != s[len(s) - i - 1] :
            isPalindrome = False
            break
    
    return isPalindrome

print(palindrome(s))