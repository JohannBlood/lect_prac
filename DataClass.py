import sys


def sloter(fields, default):
    class C:
        __slots__ = tuple(fields)
        def __init__(self):
            for i in self.__slots__:
                setattr(self, i, default)

        def __delattr__(self, name):
            setattr(self, name, default)

        def __iter__(self):
            for i in self.__slots__:
                yield getattr(self, i)

    return C


exec(sys.stdin.read())
