# 3 задание 5 варианта

def gen(st):
    while True:
        i = 0
        for j in range(1, len(st)):
            yield st[j] * i
            i += 1




# print()
for i in gen('General Kenobi'):
            print(i)