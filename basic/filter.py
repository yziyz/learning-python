"""Filter语法练习"""

if __name__ == '__main__':
    a = [-3, -2, -1, 0, 1, 2, 3]
    b = list(filter(lambda x: x > 0, a))
    for i in b:
        print(i)