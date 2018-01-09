"""Reduce语法练习"""

from functools import reduce

if __name__ == '__main__':
    a = range(100)
    b = reduce(lambda x, y: x + y, a)
    print(b)
