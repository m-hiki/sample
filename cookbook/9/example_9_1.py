# -*- coding: utf-8 -*-
"""
https://learko.github.io/books/coding/Python_Cookbook_3rd_Edition.pdf
9.1. Putting a Wrapper Around a Function
"""

import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

# Example
if __name__ == '__main__':
    countdown(100000)
    countdown(1000000)