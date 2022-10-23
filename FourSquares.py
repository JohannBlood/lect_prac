from math import sqrt

a = int(input())
mas = []
for i in range(int(sqrt(a)) + 1):
    for j in range(i, int(sqrt(a - i * i)) + 1):
        for k in range(j, int(sqrt(a - i * i - j * j)) + 1):
            for m in range(int(sqrt(a - i * i - j * j - k * k)), k - 1, -1):
                if i * i + j * j + k * k + m * m == a:
                    b = [i, j, k, m]
                    b.sort(reverse=True)
                    if b not in mas:
                        mas.append(b)
                    break
                elif i * i + j * j + k * k + m * m < a:
                    break
for i in sorted(mas):
    print(*i)
