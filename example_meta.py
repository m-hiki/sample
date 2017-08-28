
# -*- coding: utf-8 -*-

box_list = {}

class Box(type):
    def __new__(mcs, name, bases, ns, *, box_type):
        cls = type.__new__(mcs, name, bases, ns)
        if box_type:
            box_list[box_type] = cls
            cls.box_type = box_type
        return cls

    #def __init__(cls, name, bases, dct):
    #    super(BoxMetaClass, cls).__init__(name, bases, dct)
    # Required
    def __init__(self, name, bases, ns, *, box_type):
        super().__init__(name, bases, ns)

    def __str__(self):
        print('__str__')
        return super().__str__()

class FullBox(Box):
    pass

class Sub1Box(metaclass=Box, box_type='sub1'):
    def __init__(self):
        print(self.__class__.box_type)

class Sub1SubBox(Sub1Box, box_type='sb1s'):
    pass

class Sub2Box(metaclass=FullBox, box_type='sub2'):
    pass

class Sub2SubBox(Sub2Box, box_type='sb2s'):
    pass

if __name__ == "__main__":
    print(box_list)
    sub1 = box_list['sub1']()
    #sub1 = Sub1Box()
    print(str(sub1))