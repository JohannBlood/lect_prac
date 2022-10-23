k = int(input())
x = 10*k-1
a = []
while k not in a:
    a.append(k)
    print(10*k//x, sep='', end='')
    k = 10*k % x