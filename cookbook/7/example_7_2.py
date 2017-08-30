# -*- coding: utf-8 -*-
"""
https://learko.github.io/books/coding/Python_Cookbook_3rd_Edition.pdf
7.2. Writing Functions That Only Accept Keyword Arguments
"""

def recv(maxsize, *, block):
    'Receives a message'
    pass

def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

if __name__ == '__main__':
    #recv(1024, True) # TypeError
    recv(1024, block=True) # Ok


