# -*- coding: utf-8 -*-
"""
https://learko.github.io/books/coding/Python_Cookbook_3rd_Edition.pdf
8.19. Implementing Stateful Objects or State Machines
"""

class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)
    
    def new_state(self, newstate):
        self.__class__ = newstate
    
    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()
    
    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Not open')
    
    def write(self, data):
        raise RuntimeError('Not open')
    
    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Already closed')

class OpenConnection(Connection):
    def read(self):
        print('reading')
    
    def write(self, data):
        print('writing')
    
    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)

# Example
if __name__ == '__main__':
    c = Connection()
    print(c)
    #c.read()
    c.open()
    print(c)
    c.read()
    c.close()
    print(c)
    