"""
生成器

参考：
https://eastlakeside.gitbooks.io/interpy-zh/content/Generators/Generators.html
https://en.wikipedia.org/wiki/Generator_(computer_programming)
"""


def fibon(n):
    a = b = 1
    for i in range(n):
        print('i: ', i)
        # In Python, a generator can be thought of as an iterator that contains a frozen stack frame. Whenever the
        # iterator's next() method is called, Python resumes the frozen frame, which executes normally until the next
        # yield statement is reached. The generator's frame is then frozen again, and the yielded value is returned to
        # the caller.
        yield a
        a, b = b, a + b
        # 上面一行等价于下面三行
        # c = a + b
        # a = b
        # b = c
        # https://stackoverflow.com/questions/21990883/python-a-b-b-a-b


if __name__ == '__main__':
    for i in fibon(10):
        print(i)
