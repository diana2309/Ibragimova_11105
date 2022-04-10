import re
pattern = r'(?:[01][0-9]:[0-5][0-9])|(?:2[0-3]:[0-5][0-9])\s'
string = '00:59 03:15 04:20 18:30 25:60 13:71 101:02 1:14 25:45'
d = re.findall(pattern, string)

print(d)