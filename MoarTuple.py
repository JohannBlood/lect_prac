def moar(a, b, n):
    return sum(map(lambda x: x % n == 0, a)) > sum(map(lambda x: x % n == 0, b))
