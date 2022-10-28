import itertools


def seesaw(seq):
    a, b = itertools.tee(seq)
    a = filter(lambda x: x % 2 == 0, a)
    b = filter(lambda x: x % 2, b)
    yield from filter(lambda x: x != None, itertools.chain.from_iterable(itertools.zip_longest(a, b, fillvalue=None)))
