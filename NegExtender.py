import sys


class NegExt:
    def __neg__(self):
        try:
            return self.__class__(super().__neg__())
        except AttributeError:
            try:
                return self.__class__(super().__getitem__(slice(1, -1)))
            except Exception:
                return self.__class__(self)


if __name__ == '__main__':
    exec(sys.stdin.read())

