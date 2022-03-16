import os
WORKING_DIR = os.getcwd()

path = ['list.txt', '4_copy.txt', '6-generated texts']

for i in path :
    new_path = os.path.join(WORKING_DIR, i)
    if os.path.exists(new_path) :
        if os.path.isdir(new_path) :
            for item in os.listdir(new_path):
                os.remove(os.path.join(new_path, item))
            os.rmdir(new_path)
        elif os.path.isfile(new_path) :
            os.remove(new_path)