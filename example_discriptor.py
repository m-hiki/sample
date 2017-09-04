# -*- coding: utf-8 -*-


class Descriptor:
    def __init__(self, **opts):
        self.name = None
        self.value = None
        for key, value in opts.items():
            setattr(self, key, value)

    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        return self.value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    
    def read(self):
        self.value = 'hoge'

class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


class Test(metaclass=checkedmeta):
    a = Descriptor()
    b = Descriptor()

    def read(self):
        print(self.a)


if __name__ == "__main__":

    test = Test()
    test.read()
    print(test.a)
