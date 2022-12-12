import numbers
import sys
import types


def decor(fun):
    def new_f(*args, **kwargs):
        if fun.__defaults__:
            right = len(fun.__defaults__)
        else:
            right = -len(fun.__annotations__)
        for i, j in list(fun.__annotations__.items())[len(args) - 1:-right]:
            # print(i, j)
            if i not in kwargs:
                if type(j) == types.GenericAlias:
                    kwargs[i] = j.__origin__()
                    # fun.__defaults__ += (i,)
                else:
                    try:
                        kwargs[i] = j()
                        # fun.__defaults__ += (i,)
                    except:
                        kwargs[i] = None
                        # fun.__defaults__ += (i,)
        return fun(*args, **kwargs)
    return new_f


class init(type):
    def __init__(cls, name, parents, ns, **kwds):
        # print(list((i, j) for i,j in ns.items() if callable(j)))
        # # for i in inspect.getmembers(cls, predicate=inspect.ismethod):
        return super().__init__(name, parents, ns)


    @staticmethod
    def __new__(metacls, name, parents, ns, **kwds):
        for i, j in ns.items():
            if callable(j):
                # print(ns[i].__annotations__)
                ns[i] = decor(j)
        return super().__new__(metacls, name, parents, ns)

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return super().__prepare__(name, bases)


exec(sys.stdin.read())