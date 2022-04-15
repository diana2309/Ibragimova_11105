# 1 задание 5 варианта

from functools import reduce

a = [1, 2, 3, 4, 5]

def f(number):
    return str(number)
a = reduce(lambda x, y: x + y, map(f, a))

print(str(a))

# def fs(st):
#     for i in st:
#         return i
# a = '122324'
# for i in a:
#     print(i)
#
# d = reduce(filter(lambda x, y: x, map(fs, a)))
#
# print(list(d))
