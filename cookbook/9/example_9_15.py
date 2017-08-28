# -*- coding: utf-8 -*-
"""
https://learko.github.io/books/coding/Python_Cookbook_3rd_Edition.pdf
9.15. Defining a Metaclass That Takes Optional Arguments
"""

class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
    # Custom processing
        ...
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        ...
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        ...
        super().__init__(name, bases, ns)

class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    ...

# Example
if __name__ == '__main__':
    spam = Spam()
    print(spam)
