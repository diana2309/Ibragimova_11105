from functools import partial


def calculate(r1: int, st1: str, r2: int, st2: str, r3: int, st3: str, r4: int, st4: str, r5: int):
    return eval(str(r1) + st1 + str(r2) + st2 + str(r3) + st3 + str(r4) + st4 + str(r5))

def cur1_calculate(r1: int) -> callable:
    def str1_calculate(st1: str) -> callable:
        def cur2_calculate(r2: int) -> callable:
            def str2_calculate(st2: str) -> callable:
                def cur3_calculate(r3: int) -> callable:
                    def str3_calculate(st3: str) -> callable:
                        def cur4_calculate(r4: int) -> callable:
                            def str4_calculate(st4: str) -> callable:
                                def cur5_calculate(r5: int) -> int:
                                    return eval(str(r1) + st1 + str(r2) + st2 + str(r3) + st3 + str(r4) + st4 + str(r5))
                                return cur5_calculate
                            return str4_calculate
                        return cur4_calculate
                    return str3_calculate
                return cur3_calculate
            return str2_calculate
        return cur2_calculate
    return str1_calculate



d = calculate(1, '+', 1, '+', 1, '+', 1, '+', 1)
print(d)
print(cur1_calculate(1)('+')(1)('+')(1)('+')(1)('+')(1))

m = cur1_calculate(7)(8)(9)(10)(22)
m1 = m('+')('*')('/'), '-'
m2 = m('**')('-')('-'), '/'
print(m1)
print(m2)
