import re

def task014():
    with open('smth.txt', encoding='utf8') as file:
        pattern = r'\w*a+[^b]\b'
        string = file.read()
        return re.findall(pattern, string)

print(d)
