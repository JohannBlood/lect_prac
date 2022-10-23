d = dict()
while (s := input()) != '0, 0':
    x = list(map(int, s.split(', ')))
    d[x[0]] = d.get(x[0], set()) | {x[1]}
    d[x[1]] = d.get(x[1], set()) | {x[0]}
print(*sorted(map(lambda x: x[0], filter(lambda y: len(y[1]) == len(d) - 1, d.items()))))