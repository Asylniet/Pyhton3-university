def centigrade(F) :
    C = round((5 / 9) * (F - 32), 2)
    print(C)

F = int(input())
centigrade(F)