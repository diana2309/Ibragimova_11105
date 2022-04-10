import re
pattern = r'\w*a+[^b]\b'
string = 'aaab aaaac aaad ae ad b aed'
d = re.findall(pattern, string)

print(d)