"""
集合

参考：
https://eastlakeside.gitbooks.io/interpy-zh/content/set_data_structure/set_data_structure.html
https://docs.python.org/3/tutorial/datastructures.html#sets
"""

if __name__ == '__main__':
    a = {1, 2, 3}
    b = {3, 4, 5}
    # 交集
    intersection = a.intersection(b)
    print(intersection)
    print(a & b)
    # 差集
    difference = a.difference(b)
    print(difference)
    print(a - b)
    # 并集
    union = a.union(b)
    print(union)
    print(a | b)