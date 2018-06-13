from enum import Enum


class Color(Enum):
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)


if __name__ == "__main__":
    clr = Color['red']
    print(clr)
