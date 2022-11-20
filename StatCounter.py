import sys


def statcounter():
    res = dict()
    a = yield res
    while True:
        def decorator(f):
            def new_f(*args, **kwargs):
                res[f] += 1
                return f(*args, **kwargs)
            return new_f
        res[a] = 0
        #print(res)
        a = yield decorator(a)
        #print(a)


exec(sys.stdin.read())
