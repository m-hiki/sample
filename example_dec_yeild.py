
# -*- coding: utf-8 -*-
from functools import wraps

class Field:
    def __init__(self, size):
        self.size = size // 8
        self.value = None

    def read(self, file):
        pass
    
    def write(self, file):
        pass

class Int(Field):
    def read(self, file):
        print('read int')

class String(Field):
    def read(self, file):
        print('read string')


def defbox(extend):
    def _defbox(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if extend:
                for gen in extend:
                    yield gen
            for gen in func(*args, **kwargs):
                yield gen
        return wrapper
    return _defbox

@defbox(extend=None)
def box(boxtype=None):
    size = Int(32)
    typ = String(32)
    yield size
    yield typ

@defbox(extend=box())
def full_box():
    version = Int(8)
    flags = Int(24)
    yield version
    yield flags

@defbox(extend=box('ftyp'))
def file_type_box():
    major_brand = Int(32)
    minor_version = Int(32)
    compatible_brands = Int(32)
    yield major_brand
    yield minor_version
    yield compatible_brands

@defbox(extend=box('moov'))
def movie_box():
    pass

if __name__ == '__main__':
    for field in box():
        field.read('hoge')
