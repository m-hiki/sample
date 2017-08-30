# -*- coding: utf-8 -*-

class A(object):
    field = 'class field'
    def __init__(self):
        self.field = 'instance field'

if __name__ == "__main__":
    a = A()
    print(A.field)
    print(a.field)
