n = int(input())

row = 0
column = 0

for row in range(n) :
    for column in range(n) :
        if column == row :
            print(column * row, end = ' ')
        elif row == 0 :
            print(column, end = ' ')
        elif column == 0 :
            print(row, end = ' ')
        else :
            print(0, end = ' ')

    print()

#2d array miltiplication table