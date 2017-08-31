# -*- coding: utf-8 -*-

class A(object):
    field = 'class field'
    def __init__(self):
        print('Before set     : ' + self.field)
        self.field = 'instance field'
        print('After set      : ' + self.field)

if __name__ == "__main__":
    a = A()
    print('class access   : ' + A.field)
    print('instance access: ' +a.field)
