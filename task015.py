import re

def task016():
    with open('tsk14-18.txt', encoding='utf8') as file:
        pattern = r'(a+[a[^13579]*[b[2468]]+\s)|(a+[a{2}]*c{3}[b{2}]+\s)|(a+[a{2}]*c{5}[b{2}]+\s)'
        string = file.read()
        return re.findall(pattern, string)
print(d)
