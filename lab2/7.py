demons_number = int(input())
demons_dict = dict()
for i in range(demons_number) :
    a = input().split()
    if a[1] in demons_dict :
        demons_dict[a[1]] += 1
    else :
        demons_dict[a[1]] = 1    

slayer_number = int(input())
slayers_dict = dict()
for i in range(slayer_number) :
    a = input().split()
    if a[1] in slayers_dict :
        slayers_dict[a[1]] += int(a[2])
    else :
        slayers_dict[a[1]] = int(a[2])
demons = []
for key, value in demons_dict.items():
    temp = [key,value]
    demons.append(temp)

slayers = []
for key, value in slayers_dict.items():
    temp = [key,value]
    slayers.append(temp)

for i in range(len(slayers)) :
    for k in range(len(demons)) :
        if slayers[i][0] == demons[k][0] and slayers[i][1] > 0:
            demons[k][1] -= slayers[i][1]
            slayers[i][1] -= 1
               
sum = 0
for j in range(len(demons)) :
    if demons[j][1] > 0 :
        sum += demons[j][1]

print(f'Demons left: {sum}')


#slayers and demons