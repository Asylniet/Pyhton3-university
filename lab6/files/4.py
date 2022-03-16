# with open('4.txt', 'a') as f :
#     for i in range(11) :
#         f.writelines([f'Line{i} \n'])

with open('4.txt', 'r') as f :
    arr = f.readlines()

print(len(arr))