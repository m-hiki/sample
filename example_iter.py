# -*- coding: utf-8 -*-


if __name__ == "__main__":
    alphabet_iterator = iter('abcdefghijklmnopqrstuvwxyz')
    print(next(alphabet_iterator))
    print(next(alphabet_iterator))
    print(next(alphabet_iterator))
    print(next(alphabet_iterator))

    print('iterator with sentinel')
    alphabet_iterator = iter('abcdefghijklmnopqrstuvwxyz')
    iterator_with_sentinel = iter(lambda:next(alphabet_iterator), 'm')    
    print(''.join(iterator_with_sentinel))