# -*- coding: utf-8 -*-

class Field:
    def __init__(self, size):
        self.size = size
        self.value = None
    
    def read(self, file):
        pass

class IntField(Field):
    def read(self, file):
        #self.value = int.from_bytes(file.read(1), ord='big')
        print(file)

def outer_func(size):
    obj = IntField(size)
    return obj

if __name__ == '__main__':
    x = outer_func(16)
    print(x.read('file'))
