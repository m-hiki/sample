

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(B):
    pass

class F(C):
    pass

class G(C):
    pass

def get_class_list(cls, res=[]):
    subclasses = getattr(cls, '__subclasses__')()
    for subclass in subclasses:
        get_class_list(subclass, res)
    res.append(cls)
    return res

if __name__ == "__main__":
    res = get_class_list(A)
    for cls in res:
        print(cls.__name__)
        print(type(cls.__base__))
