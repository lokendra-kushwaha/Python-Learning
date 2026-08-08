import functools

S = 'lokendra'
char = []
for i in S:
    char.append(ord(i))

minchar = functools.reduce(lambda x, y: x if x < y else y, char)
print(chr(minchar))