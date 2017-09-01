# -*- coding: utf-8 -*-
"""
https://learko.github.io/books/coding/Python_Cookbook_3rd_Edition.pdf
8.13. Implementing a Data Model or Type System
"""

# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        #print('Descriptor.__init__')
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        #print('Descriptor.__set__')
        print('----')
        print(self)
        print(self.name)
        print(instance)
        print(value)
        instance.__dict__[self.name] = value
        print(instance.__dict__)
        print('----')

# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)

# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Float, Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString(String, MaxSized):
    pass

class Stock:
    # Specify constraints
    #name = SizedString('name',size=8)
    #shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    hoge = UnsignedFloat('hoge')
    
    def __init__(self, name, shares, price):
        #print('Stock.__init__')        
        self.name = name
        self.shares = shares
        self.price = price

# Class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate

@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock2:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


class Stock3(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
# Example
if __name__ == '__main__':
    a = Stock('ACME', 50, 91.1)
    #print(a.name)
    #b = Stock('AAPL', 100, 110.0)
    #print(a.__dict__)
    #print(a.hoge)
    a.hoge = 100.0
    print(a.price)
    print(a.hoge)
    #s.shares = -10
    #s.price = 'a lot'
    #s.name = 'ABRACADABRA'