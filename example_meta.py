
# -*- coding: utf-8 -*-


class BoxMeta(type):
    box_list = {}
    
    def __new__(mcs, clsname, bases, clsdict, *, box_type):
        clsdict['box_type'] = box_type
        cls = type.__new__(mcs, clsname, bases, clsdict)        
        if box_type:
            mcs.box_list[box_type] = cls
        return cls

    def __init__(self, clsname, bases, clsdict, *, box_type):
        super().__init__(clsname, bases, clsdict)

        
class Box(metaclass=BoxMeta, box_type=None):

    Field()

    def read(self, file):
        print(self.box_type)
        print(self.__dict__.keys())
    


class FullBox(Box, box_type=None):
    pass

class Field:
    def read(self):
        print('read')
    
    def write(self):
        print('write')


class IntField(Field):
    pass

class StringField(Field):
    pass

class Sub1Box(Box, box_type='sub1'):
    def __init__(self):
        print(self.__class__.box_type)

class Sub1SubBox(Sub1Box, box_type='sb1s'):
    pass

class Sub2Box(FullBox, box_type='sub2'):
    pass


class Sub2SubBox(Sub2Box, box_type='sb2s'):
    pass

if __name__ == "__main__":
    #print(Box.box_list)
    #sub1 = Box.box_list['sub1']()
    sub1 = Sub1Box()
    sub1.read('hoge')
    #print(str(sub1))