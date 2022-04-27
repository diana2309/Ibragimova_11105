# по привычке назвала задание на 1 контрольной как задание из домашки и теперь в файле task003 код третьего задания контрольной

lst = []
res = []
for e in input().split():
    if e in '+-*/':
        a = lst[-2]
        b = lst[-2]
        lst.pop()
        lst.pop()
        if e == '+':
            res.append(f'({a}+{b})')
            # print(lst)
        elif e == '-':
            res.append(f'({a}-{b})')
        elif e == '*':
            res.append(f'({a}*{b})')
        elif e == '/':
            res.append(f'({a}/{b})')
            # print(lst)
        lst.append(res[-1])
    else:
        lst.append(e)
        # print(lst)
print(*res[-1])