a = eval(input())
b = []
for i in a:
    if type(i) == tuple:
        for j in i:
            b.append(j)
    else:
        if len(b) >= i:
            c = []
            for k in range(i):
                c.append(b.pop(0))
            print(tuple(c))
        else:
            break