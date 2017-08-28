# -*- coding: utf-8 -*-
"""
https://learko.github.io/books/coding/Python_Cookbook_3rd_Edition.pdf
4.1 Manually Consuming an Iterator
"""
with open('./passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
