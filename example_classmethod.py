# -*- coding: utf-8 -*-

class A(object):

    @classmethod
    def class_method(cls):
        print(cls)

    @staticmethod
    def static_method():
        print('static')

if __name__ == "__main__":
    A.class_method()
    A().class_method()
    A.static_method()
    A().static_method()