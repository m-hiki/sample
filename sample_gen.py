# -*- coding: utf-8 -*-
def seq1(maxnum):
    i = 0
    while True:
        i = 0 if i >= maxnum else i + 1
        yield i

def seq2():
    yield from range(100)

def seq3():
    yield from 'abcdefghijklmnopqrstuvwxyz'

if __name__ == "__main__":
    seq = seq1(3)
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print('----')
    seq = seq2()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print('----')
    seq = seq3()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print('----')
    seq = (lambda: (yield from 'abcdefghijklmnopqrstuvwxyz'))()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    