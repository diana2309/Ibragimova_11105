
lis = ['uhk', 'rduiju', 'fdfoo', 'ssshhhiiittt', 'sttt', 'foo']


def check_foo_word(fc):
    for j in fc:
        if 'foo' in j:
            yield j

def check_symbols(symbols):
    count = 0
    for k in range(1, len(symbols)):
        if symbols[k-1] != symbols[k]:
            count += 1
    return count

def register_change(l):
    lst = []
    for i in l:
        if i[0] == i[0].upper():
            lst.append(i[0].lower() + i[1:])
        else:
            lst.append(i[0].upper() + i[1:])
    return lst


d = list(filter(lambda x: check_symbols(x)>= 3, lis))
print(register_change(d))

print(sum(list(map(len, list(check_foo_word(lis))))))

