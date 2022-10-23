mas = []
minx, miny, maxx, maxy = 0, 0, 0, 0
while (s := input()):
    name, fname, *team = s.split()[:-1]
    team = ' '.join(team)
    mas.append(([name, fname, team], list(map(int, s.split()[-1].split(':')))))
#print(*sorted(mas, key=lambda x: [x[1], x[0][1], x[0][0], x[0][2]]), sep='\n')
mas = sorted(mas, key=lambda x: [x[1], x[0][1], x[0][0], x[0][2]])
i, k = 0, 0
prev = []
nlen = max(map(len, [x[0][0] for x in mas]))
flen = max(map(len, [x[0][1] for x in mas]))
tlen = max(map(len, [x[0][2] for x in mas]))
for k in mas:
    if k[1] != prev:
        #print('wtf')
        i += 1
        prev = k[1]
    if i <= 3:
        print(k[0][0].ljust(nlen), k[0][1].ljust(flen), k[0][2].ljust(tlen), ':'.join(map(str, k[1])))
    else:
        break