import os

# WORKING_DIR = os.getcwd()
WORKING_DIR = '/Users/asylniet/Documents/Python/lab6'
mode = int(input('Choose mode. What to display? \n1 - Only directories \n2 - Files and all directories \n3 - Just files \n'))


for item in os.listdir(WORKING_DIR):
    target_path = os.path.join(WORKING_DIR, item)
    if mode == 1 or mode == 2 :
        if os.path.isdir(target_path):
            print(f'DIR: {item}')
            if mode == 2 :
                for item2 in os.listdir(target_path):
                    print('-'*6, item2)
    else :
        if os.path.isfile(target_path):
            print(f'FILE: {item}')