import os
str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

WORKING_DIR = os.getcwd()
if not os.path.exists('6-generated texts'):
    os.mkdir('6-generated texts')

new_path = target_path = os.path.join(WORKING_DIR, '6-generated texts')
os.chdir(new_path)

for i in str :
    with open(f'{i}.txt', 'a') as f :
        f.write(i)