import math


a, b, c = eval(input())
d = b * b - 4 * a * c
if a == b == c == 0:
    print(-1)
elif d < 0:
    print(0)
elif d == 0:
    print(-b / (2 * a))
else:
    print(*sorted([(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]))