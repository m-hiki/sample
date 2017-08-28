
# -*- coding: utf-8 -*-

box_list = {}

class BoxMetaClass(type):
    def __new__(mcs, name, bases, dict):
        cls = type.__new__(mcs, name, bases, dict)
        if cls.box_type:
            box_list[cls.box_type] = cls
        return cls

    #def __init__(cls, name, bases, dct):
    #    super(BoxMetaClass, cls).__init__(name, bases, dct)

    def __str__(self):
        print('__str__')
        return super().__str__()

class Box(object, metaclass=BoxMetaClass):
    box_type = None

    def __init__(self, size=None):
        self.size = size
        self.body = []

    def __str__(self):
        
        rep = self.__class__.box_type +'(' + self.size + ')'
        return rep

    def def_element(self, element):
        self.body.append(element)

class Element():
    def __init__(self, name, element_type, element_size):
        self.name = name
        self.element_type = element_type
        self.element_type = element_type

class Sub1Box(Box):
    box_type = 'sub1'

class Sub1SubBox(Sub1Box):
    box_type = 'sb1s'

class Sub2Box(Box):
    box_type = 'sub2'

class Sub2SubBox(Sub2Box):
    box_type = 'sb2s'

if __name__ == "__main__":
    print(box_list)
    sub1 = box_list['sub1']()
    #sub1 = Sub1Box()
    print(str(sub1))