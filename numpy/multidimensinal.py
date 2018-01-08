import numpy as np


def f(x: int, y: int):
    return 10 * x + y


if __name__ == '__main__':
    a = np.fromfunction(f, (4, 4), dtype=int)
    print(a)
    print(a[-1])
    print(a[2, 3])

    b = a[:, 1]
    print(b)

    for row in a:
        print(row)

    for element in a.flat:
        print(element)