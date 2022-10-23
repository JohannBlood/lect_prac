def ADD(f, g):
    def a(x):
        return f
    def b(x):
        return g
    if callable(f):
        a = f
    if callable(g):
        b = g
    return lambda x: a(x) + b(x)


def SUB(f, g):
    def a(x):
        return f
    def b(x):
        return g
    if callable(f):
        a = f
    if callable(g):
        b = g
    return lambda x: a(x) - b(x)


def MUL(f, g):
    def a(x):
        return f
    def b(x):
        return g
    if callable(f):
        a = f
    if callable(g):
        b = g
    return lambda x: a(x) * b(x)


def DIV(f, g):
    def a(x):
        return f
    def b(x):
        return g
    if callable(f):
        a = f
    if callable(g):
        b = g
    return lambda x: a(x) / b(x)
