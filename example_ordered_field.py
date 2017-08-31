
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

    def read(self, current_class=Base, terminal_class=None):
        ####
        for name, field in self.fields.items():
            field.read(name)
        ####
        print(SubSub.__base__)
        if current_class == Base:
            self.read(current_class=SubSub.__base__, terminal_class=SubSub)

class Sub(Base):
    d = SubField()
    e = SubField()
    f = SubField()

class SubSub(Sub):
    g = SubField()
    h = SubField()
    i = SubField()


if __name__ == "__main__":
    #print(BaseOrderiedField.__ordered__)

    field = Base()
    field.read()
    #print(OrderiedField.__ordered__)