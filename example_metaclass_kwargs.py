

class FieldMeta(type):
    def __new__(cls, name, bases, namespace):
        return type.__new__(cls, name, bases, namespace)

        
class Field(metaclass=FieldMeta):
    def __init__(self, size=None):
        if size:
            self.size = size // 8 # bit to byte
        self.value = None

    def read(self, file):
        pass

    def write(self, file):
        pass

class Int(Field):
    def read(self, file):
        print('read int')
        #self.value =  int.from_bytes(file.read(self.size), byteorder='big')

class List(Field):
    def __init__(self, size, obj):
        super().__init__(size)
        self.obj = obj

    def read(self, file):
        self.value = []
        for _ in range(self.size):
            item = deepcopy(self.obj)
            item.read(file)
            self.value.append(item)

class Entry(Field):
    def __init__(self, count, **args):
        super().__init__(None)
        self.count = count
        self.objs = dict(args)

    def read(self, file):
        self.value = []
        count = deepcopy(self.count)
        count.read(file)
        for _ in range(count.value):
            items = {}
            for name, obj in self.objs.items():
                item = deepcopy(obj)
                item.read(file)
                items[name] = item
            self.value.append(item)

class Item(Field):
    offset_size = Int(8)
    length_size = Int(8)
    extent_count = Int(16)
    extents = Entry(count=extent_count,
                    extent_offset = Int(offset_size.value),
                    extent_length = Int(length_size.value))

if __name__ == "__main__":
    item = Item()
    item.read(file)