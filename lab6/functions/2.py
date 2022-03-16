string = input()

upper = 0
lower = 0

for i in string :
    if i.isupper() :
        upper += 1
    else :
        lower += 1


print(f'uppercases - {upper}, lowercase - {lower}')