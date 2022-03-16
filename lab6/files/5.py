arr = ['a', 'b', 'c', 'd', 'e']
with open('list.txt', 'a') as f :
    for i in arr :
        f.write(f'{i}\n')