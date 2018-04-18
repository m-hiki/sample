# -*- coding: utf-8 -*-


class FieldMeta(type):
    def __new__(cls, name, bases, namespace):
        clsobj = type.__new__(cls, name, bases, namespace)
        print('FieldMeta.__new__ : ' + name)
        # for name, attr in namespace.items():
        #    print(name + ' : ' + str(attr))
        return clsobj

    def __init__(self, name, bases, namespace):
        super().__init__(name, bases, namespace)
        print('FieldMeta.__init__ : ' + name)

    def __get__(self, instance, owner):
        print('FieldMeta.__get__ ')


class Field(metaclass=FieldMeta):
    typ = 'string'
    name = 'default'

    def __init__(self, name):
        self.name = name
        self.value = None
        print('Field.__init__ : ' + name)


class Outer(Field):
    outer_a = Field('outer_a')
    outer_b = Field('outer_b')

    class Inner(Field):
        inner_a = Field('inner_a')
        # inner_d = Outer.outer_b  # name 'Outer' is not defined

    outer_c = Inner('outer_c')


if __name__ == "__main__":
    outer = Outer('outer')
