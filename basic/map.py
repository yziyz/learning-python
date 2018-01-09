"""Map语法练习"""

if __name__ == '__main__':
    a = range(3)
    b = list(map(lambda x: x ** 2, a))
    for i in b:
        print(i)
