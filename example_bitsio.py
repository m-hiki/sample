
# -*- coding: utf-8 -*-
from io import BytesIO


class BitsIO(BytesIO):
    """BitsIO
       msb first
    """
    def __init__(self, file):
        super().__init__(file)
        self.value = 0
        self.left = 8

    def read_byte(self):
        return int.from_bytes(self.read(1), byteorder='big')

    def read_bits(self, size=1):
        read_len = size - self.left
        if read_len <= 0:
            if self.left == 8:
                self.value = self.read_byte()

            self.left = 8 if self.left == 0 else -read_len
            mask = (1 << size) - 1
            return (self.value >> self.left) & mask
        else:
            return (self.read_bits(size - 8) << 8) | self.read_byte()


if __name__ == '__main__':
    file = BitsIO(b'\x0f\xff\x00\xff')
    #print(file.read_bits(4))
    print(format(file.read_bits(32), 'b'))
