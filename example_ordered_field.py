
# -*- coding: utf-8 -*-
from collections import OrderedDict


class OrderedFieldMeta(type):
    # https://www.python.org/dev/peps/pep-3115/
    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()

    def __new__(mcs, name, bases, clsdict):
        cls = type.__new__(mcs, name, bases, dict(clsdict))
        fields = ((k, v) for k, v in clsdict.items() if isinstance(v, Field))
        cls.fields = OrderedDict(fields)
        return cls


class Field():
    def read(self, name):
        print('feild read ' + name)

class SubField(Field):
    def read(self, name):
        print('subfeild read ' + name)
        
class Base(metaclass=OrderedFieldMeta):
    a = Field()
    b = SubField()
    c = SubField()

    def read_field(self, file):
        for name, field in self.fields.items():
            field.read(name)

    def read(self, file):
        self.read_field(file)
        for cls in get_class_tree(Base, SubSub):
            self.__class__ = cls
            self.read_field(file)        

class Sub(Base):
    d = SubField()
    e = SubField()
    f = SubField()

class SubSub(Sub):
    g = SubField()
    h = SubField()
    i = SubField()


def get_class_tree(base, target):
    tree=[]
    while target != base:
        tree.insert(0, target)
        target = target.__base__
    return tree

def get_class_tree_yeild(base, target):
    while target != base:
        yield target
        target = target.__base__


if __name__ == "__main__":
    #print(BaseOrderiedField.__ordered__)

    a = Base()
    a.read('hoge')

    b = Base()
    b.read('hoge')
    #print(OrderiedField.__ordered__)
