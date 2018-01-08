import numpy as np

if __name__ == '__main__':
    a = np.arange(10) ** 2
    print(a)
    print(a[2])
    print(a[3:-1])

    a[:-1] = 1000
    print(a)

    print(a[::-1])

    for i in a:
        print(i ** (1/2.))