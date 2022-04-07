def gen_str(st: str):
    a = len(st)
    i = 0
    while True:
        while i != a:
            yield st[i]
            i += 1
            if i == a:
                for j in st[::-1]:
                    yield j

        i = 0

d = gen_str('qw')
for i in range(7):
    print(next(d), end=' ')