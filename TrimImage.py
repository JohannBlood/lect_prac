mas = []
minx, miny, maxx, maxy = 0, 0, 0, 0
while (s := input()):
    cor = list(map(int, s.split()[:-1]))
    if cor[2] != 0 and cor[3] != 0:
        if cor[2] < 0:
            cor[0] += cor[2]
            cor[2] = 0 - cor[2]
        if cor[3] < 0:
            cor[1] += cor[3]
            cor[3] = 0 - cor[3]
        maxx = max(maxx, cor[0] + cor[2])
        maxy = max(maxy, cor[1] + cor[3])
        mas.append((cor, s.split()[-1]))
minx = min(i[0][0] for i in mas)
miny = min(i[0][1] for i in mas)
image = [['.' for i in range(maxx - minx)] for j in range(maxy - miny)]
for i in mas:
    cor = i[0]
    for j in range(cor[1] - miny, cor[1] - miny + cor[3]):
        for k in range(cor[0] - minx, cor[0] - minx + cor[2]):
            image[j][k] = i[1]
for i in image:
    print(*i, sep='')
