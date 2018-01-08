import numpy as np

if __name__ == '__main__':
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    # 减法
    c = a - b
    print(c)
    # 平方
    d = a ** 2
    print(d)
    # 矩阵乘法
    e = np.dot(a, b)
    print(e)
    # 随机
    f = np.random.random((1, 20))
    print(f.std())
    print(f.cumsum())

    g = np.arange(3)
    print(np.exp(g))
    print(np.sqrt(g))
