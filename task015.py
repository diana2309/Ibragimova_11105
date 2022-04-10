import re
pattern = r'(a+[a[^13579]*[b[2468]]+\s)|(a+[a{2}]*c{3}[b{2}]+\s)|(a+[a{2}]*c{5}[b{2}]+\s)'
string = 'b a ab aaabbb aaacccbbbb aaaccccbbbb aaacccccbb aaaabb aaaaabb'
d = re.findall(pattern, string)
print(d)