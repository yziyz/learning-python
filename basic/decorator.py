"""
装饰器

https://eastlakeside.gitbooks.io/interpy-zh/content/decorators/your_first_decorator.html
"""


def a_decorator(a_func):
    def wrap():
        print('Wrapped')
        a_func()

    return wrap


@a_decorator
def hello():
    print('hello')


if __name__ == '__main__':
    hello()
