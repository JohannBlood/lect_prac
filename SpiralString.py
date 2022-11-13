from collections import defaultdict

def define_field_size(s):
    if not s:
        return 0, 0, 0, 0, []
    count, c, size = 0, 2, 0
    x, y = 2, 1
    cx , cy = 0, 0
    a = []
    while size < len(s):
        if not count:
            count += 1
            t1 = size
            size = 2
            a.append(range(t1, size))
        else:
            count += 1
            t1 = size
            size += c
            a.append(range(t1, size))
            c += 1
            if count % 2 == 0:
                y += 2
            else:
                x += 2
            if (count - 2) % 4 == 0:
                cy += 2
            elif (count - 2) % 4 == 1:
                cx += 2
    a[-1] = a[-1][:len(s)]
    return x, y, cx, cy, a



class Spiral:

    def __init__(self, s):
        s = list(s)
        tt = defaultdict(int)
        for i in s:
            tt[i] += 1
        ttt = ""
        for k, v in tt.items():
            ttt += k * v

        self.buff = ttt
        x, y, self.xc, self.yc, self.a = define_field_size(self.buff)
        self.field = [[" " for _ in range(x)] for _ in range(y)]

    def draw1(self):
        direct = {
            0: (1, 0),
            1: (0, -1),
            2: (-1, 0),
            3: (0, 1)
        }
        xc, yc = self.xc, self.yc
        minx, maxx, miny, maxy = len(self.field[0]), 0, len(self.field), 0
        for i, it in enumerate(self.a):
            for j in it:
                if j >= len(self.buff):
                    break
                self.field[yc][xc] = self.buff[j]

                minx = min(minx, xc)
                maxx = max(maxx, xc)
                miny = min(miny, yc)
                maxy = max(maxy, yc)
                xc += direct[i % 4][0]
                yc += direct[i % 4][1]
            xc -= direct[i % 4][0]
            yc -= direct[i % 4][1]
            xc += direct[(i + 1) % 4][0]
            yc += direct[(i + 1) % 4][1]

        for i in range(len(self.field)):
            if i > maxy or i < miny:
                for j in range(len(self.field[0])):
                    self.field[i][j] = ""

        for i in range(len(self.field[0])):
            if i > maxx or i < minx:
                for j in range(len(self.field)):
                    self.field[j][i] = ""



    def __str__(self):
        self.draw1()
        ans = ""
        for line in self.field:
            t = "".join(line)
            if t:
                ans += "".join(line).rstrip() + '\n'
        return ans[:-1]

    def __add__(self, other):
        return Spiral(self.buff + other.buff)

    def __sub__(self, other):
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in self.buff:
            d1[i] += 1
        for j in other.buff:
            d2[j] += 1
        for key in d1:
            d1[key] -= d2[key]
        tmp = ""
        for key, val in d1.items():
            if val > 0:
                tmp += key * val
        return Spiral(tmp)

    def __mul__(self, other):
        return Spiral(self.buff * other)

    def __getitem__(self, item):
        return self.buff[item]