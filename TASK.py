import collections
from functools import reduce

file = open('text.txt', 'r', encoding='utf-8')
words = file.read().replace('\n', ' ').split()
words = [word.strip('.,!;()[]?:') for word in words]
new_words = []

for word in words:
    new_words.append(word.lower())


uniq_dict = {}
for i in new_words:
    uniq_dict[i] = uniq_dict.setdefault(i, 0) + 1

# print(uniq_dict)
uniq = len(list(filter(lambda x : uniq_dict[x] == 1, uniq_dict)))


alf = {'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'э', 'ю', 'я',}
for k in file:
    count = 0
    for word in words:
        for i in alf:
            if word[0] == i:
                count += 1
                print(f'{i}:{format(count)}')

count = collections.Counter(new_words)
most_common = count.most_common()[0]
print(most_common)

the_longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(the_longest)

def shift(word):
    if len(word)%2 == 1:
        s = word
        n = 1
        print(s[n % len(s):] + s[:n % len(s)])

    else:
        n = len(word) - 1
        sh = list(word)
        for i in range(n):
            sh.insert(len(sh), sh.pop(0))

        print(''.join(sh))

with open('text.txt', 'a', encoding='utf-8') as file1:
    file1.write(f'\n{uniq}\n\n')
    file1.write(f'{most_common}\n\n')
    file1.write(f'{the_longest}\n\n')
    for word in words:
        if len(word) > 4:
            file1.write(shift(word))
