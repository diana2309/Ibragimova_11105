def gen_degrees(s):
    a = int(input())
    while a >= 0:
        yield s**a
        a -= 1



g = gen_degrees(7)
print(sorted(list(g)))

def gen_even(s):
    while s > 0:
        if s%10%2 == 0:
            yield s%10
            s = s//10
        else:
            s = s//10

g = gen_even(245637489)
print(list(g))

# import time
# start_time = time.time()
def gen_simple(s):
    for i in range(1, s+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                yield i

g = gen_simple(45)
print(list(g))
# end_time = time.time()
# print("Elapsed Time: " + str(end_time-start_time))



def gen_simple_in_s(s):
    asd = [2, 3, 5, 7]
    asd1 = []
    for i in asd:
        if str(i) in str(s):
            asd1.append(i)

    for i in range(1, s):
        for j in asd1:
            if i % j == 0:
                yield i


g = gen_simple_in_s(57)
print(sorted(list(g)))
