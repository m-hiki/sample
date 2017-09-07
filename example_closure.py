# -*- coding: utf-8 -*-
import sys


def def_int(size):
    value = None

    def func():
        return value

    def read(file):
        nonlocal value
        print(file + '.read(' + str(size) + ')')

    def write(file):
        print(file + '.write(' + str(size) + ') : ' + str(value))
    
    def set(v):
        nonlocal value
        value = v
        
    func.read = read
    func.write = write
    func.set = set
    return func

def loop(size, target):
    value = []

    def func():
        return value

    def read(file):
        nonlocal value
        value = []
        print(file + '.read(' + str(size) + ')')

    def write(file):
        print(file + '.write(' + str(size) + ') : ' + str(value))
    
    def set(v):
        nonlocal value
        value = v
        
    func.read = read
    func.write = write
    func.set = set
    return func

if __name__ == "__main__":
    size = def_int(32)
    size.read('hoge')
    print(size())
    size.set(20)
    print(size())
    size.write('hoge')
    