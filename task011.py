"""global"""
a = int(input())

def exponentiation(digits_after_point, u, i):
    """local"""
    t = float(input())
    counter = str(t)


    def work_search():
        """local"""
        res = abs(counter.find('.') - len(counter)) - 1
        if res < digits_after_point:
            print('Округление не получится')
        else:
            """Enclosure"""
            return round(t, digits_after_point) * u * i
        return work_search()


    exh = work_search()
    # print(exh)
    """global"""
    global a
    if a > 0:
        """Enclosure"""
        return exh ** a
    else:
       return 'ошибка'




d = exponentiation(0, 1, 1)
print(d)




