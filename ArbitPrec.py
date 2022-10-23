from decimal import Decimal, getcontext


foo = input()
func = lambda x: eval(foo)
d = int(input())
getcontext().prec = d + 2
x = [Decimal(-1.5), Decimal(1.5)]
eps = Decimal(f"1E-{d + 1}")
length = lambda x: x[-1] - x[0]
flag = func(x[0]) < 0
s = "{:." + str(d) + "f}"
while length(x) > eps:
    t = (x[0] + x[-1]) / 2
    if func(t) == 0:
        print(s.format(t))
        break
    elif func(t) > 0 and flag or func(t) < 0 and not flag:
        x = [x[0], t]
    elif func(t) < 0 and flag or func(t) > 0 and not flag:
        x = [t, x[-1]]
else:
    print(s.format(x[1]))