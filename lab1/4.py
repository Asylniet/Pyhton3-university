x = int(input())
z = str(input())
if z == 'k' :
    c = int(input())
    print(f'%.{c}f' % float(x / 1024))
elif z == 'b' :
    print(x * 1024)


#bite to kilo and vice versa