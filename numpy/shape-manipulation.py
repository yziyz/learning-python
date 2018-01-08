import numpy as np

if __name__ == '__main__':
    a: np.ndarray = np.floor(10 * np.random.random((3, 4)))
    print(a)
    print(a.shape)
    print("a.ravel(): \n", a.ravel())
    print("a.ravel(order='F'): \n", a.ravel(order='F'))
    print(a.flat)
    print(a.reshape(6, 2))
    print(a.transpose())
