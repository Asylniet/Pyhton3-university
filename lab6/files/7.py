with open('4.txt', 'r') as mainFile, open('4_copy.txt', 'a') as copyFile:
    for line in mainFile :
        copyFile.write(line)