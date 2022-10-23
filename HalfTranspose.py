a = list(eval(input()))
b = []
b.append(a)
d = []
for i in range(len(a) - 1):
    b.append(list(eval(input())))
for i in range(len(a)):
    c = []
    for j in range(i + 1):
        c.append(b[i][j])
    for j in range(i - 1, -1, -1):
        c.append(b[j][i])
    d.append(c)
for i in d:
    print(*i, sep=',')