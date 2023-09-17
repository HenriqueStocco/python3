# count é um iterator sem fim

from itertools import count

#   começa, de quanto em quanto
# c1 = count(8, 8)
# Pode passar **kwargs
c1 = count(step=8, start=8)

#   começa, até onde, de quanto em quanto
r1 = range(8, 100, 8)

# print(next(c1))
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('count')
for c in c1:
    if c >= 100:
        break
    print(c)
print()
print('range')
for r in r1:
    print(r)