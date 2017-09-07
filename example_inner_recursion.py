# -*- coding: utf-8 -*-
# PEP 3104
def enclosing_function():
    def factorial(n):
        if n < 2:
            return 1
        return n * factorial(n - 1)  # fails with NameError
    print factorial(5)

if __name__ == "__main__":
    enclosing_function()