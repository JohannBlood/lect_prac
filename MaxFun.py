def maxfun(s, *funcs):
    mas = [sum(map(i, s)) for i in funcs]
    return funcs[::-1][mas[::-1].index(max(mas))]


