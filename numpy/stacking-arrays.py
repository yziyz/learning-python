import numpy as np

if __name__ == '__main__':
    a = np.arange(start=0, stop=8, step=1).reshape(2, 4)
    print(a)
    b = np.arange(start=8, stop=16, step=1).reshape(2, 4)
    print(b)
    # Stack arrays in sequence vertically (row wisely)
    print(np.vstack((a, b)))
    # Stack arrays in sequence horizontally (column wise).
    print(np.hstack((a, b)))

    c = np.column_stack((a, b))
    print(c)

    print(a[:, np.newaxis])
