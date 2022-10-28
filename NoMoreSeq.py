def nomore(seq):
    yield from [j for i in seq for j in seq if j <= i]

