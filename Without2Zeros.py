def No_2Zero(n, k):
    res = 0
    for i in range(k ** (n - 1), k ** n):
        a = i
        x = n - 1
        c = 0
        while x >= 0:
            if a >= k ** x:
                c = 0
                a %= k ** x
                x -= 1
            else:
                if a == 0 and x >= 1:
                    break
                c += 1
                x -= 1
            if c == 2:
                break
        else:
            res += 1
    return res


print(No_2Zero(30, 30))