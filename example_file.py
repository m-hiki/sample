# -*- coding: utf-8 -*-
import os


if __name__ == "__main__":
    filename = 'test.txt'
    filesize = os.path.getsize(filename)
    file = open(filename, 'rb')
    readsize = filesize
    print('filesize :' + str(filesize))
    try:
        length = 3
        while readsize > 0:
            print(str(readsize) + ' ' + str(length))
            print(file.read(length).decode())
            readsize -= length
            length += 1
    finally:
        file.close()
    print('readsize :' + str(readsize))
