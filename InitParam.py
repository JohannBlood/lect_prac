import numbers
import types


def decor(fun):
    def new_f(*args, **kwargs):
        # print(fun.__defaults__)
        for i, j in list(fun.__annotations__.items())[len(args) - 1:]:
            if i not in fun.__defaults__ and i not in kwargs:
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


class C(metaclass=init):
    def __init__(self, var: int, rng: range, lst: list[int], defined: str = "defined"):
        self.data = f"{var}/{rng}/{lst}/{defined}"

for c in (C(), C(1, range(3)), C(rng=range(4, 7)), C(lst=[1, 2, 3], defined=3)):
    print(c.data)