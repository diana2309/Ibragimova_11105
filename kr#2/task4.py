# 4 задание 5 варианта
import re

pattern = r'\b(?:)q\w*e\b'
string = 'qdfbsjdeeee weql'
print(re.findall(pattern, string))
