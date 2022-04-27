import re

def task017():
    with open('tsk14-18.txt', encoding='utf8') as file:
        pattern = r'[А-Я]+[^а-я]+'
        string = file.read()
        return re.findall(pattern, string)

print(task017())
