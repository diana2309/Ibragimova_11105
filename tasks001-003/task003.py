# по привычке назвала задание на 1 контрольной как задание из домашки и теперь в файле task003 код третьего задания контрольной

lst = []
res = []
n = input().split()
for e in n:
    if e not in ['+', '-', '*', '/', 'A', 'B', 'C']:
        print('ошибка')
    if e in ['+', '-', '*', '/']:
        first = lst[-2]
        second = lst[-1]
        lst.append(first)
        lst.append(second)
        # print(lst)
        if e == '+':
            res.append(f'({first}+{second})')
        elif e == '-':
            res.append(f'({first}-{second})')
        elif e == '*':
            res.append(f'({first}*{second})')
        elif e == '/':
            res.append(f'({first}/{second})')
        lst.append(res[-1])
    else:
        lst.append(e)
print(res[-1])
