def get_permutation(string, i = 0):

    if i == len(string):   	 
        if string == None :
            print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
        get_permutation(words, i + 1)

s = input()
get_permutation(s)