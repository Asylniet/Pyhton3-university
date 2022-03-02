def squares(n, max) :
    while n <= max :
        yield n**2
        n += 1

n = int(input("Enter the starting number: \n"))
max = int(input("Enter the final number: \n"))
squares_list = list(squares(n, max))
print(*squares_list)