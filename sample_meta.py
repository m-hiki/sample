

class SampleMeta(type):
    pass


class Box(object):
    def __init__(self, box_type):
        self.box_type = box_type


class HogeBox(Box):
    pass

class FooBox(Box):
    pass

