import re

def task015():
    with open('smth.txt', encoding='utf8') as file:
        pattern = r'(?:[01][0-9]:[0-5][0-9])|(?:2[0-3]:[0-5][0-9])\s'
        string = file.read()
        return re.findall(pattern, string)

print(d)
