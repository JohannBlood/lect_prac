import numbers
import sys


def decor(fun, arg):
    def new_f(*args, **kwargs):
        res = fun(*args, **kwargs)
        return round(res, arg) if isinstance(res, numbers.Real) else res
    return new_f


class fixed(type):
    def __init__(cls, name, parents, ns, **kwds):
        # print(list((i, j) for i,j in ns.items() if callable(j)))
        # # for i in inspect.getmembers(cls, predicate=inspect.ismethod):
        return super().__init__(name, parents, ns)


    @staticmethod
    def __new__(metacls, name, parents, ns, ndigits=3):
        # print(metacls, eval(name))
        # import inspect
        # inspect.getmembers(eval(name), predicate=inspect.ismethod)
        for i, j in ns.items():
            if callable(j):
                ns[i] = decor(j, ndigits)
        return super().__new__(metacls, name, parents, ns)

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return super().__prepare__(name, bases)


exec(sys.stdin.read())