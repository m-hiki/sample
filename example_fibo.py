
def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, y + x


def fibonacci2():
    x, y = 0, 1
    yield from map(lambda: y + x, range(100))


if __name__ == "__main__":
    f = fibonacci()
    n = 0
    n_1 = n
    for v in range(100):
        n = f.__next__()
        r = n/n_1 if n_1 != 0 else 0
        print('{0} {1}'.format(n, r))
        n_1 = n
