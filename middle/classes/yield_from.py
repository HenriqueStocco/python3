# yield from -> 

def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')

def gen3():
    print('COMEÇOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')

def gen2(gen=None):
    print('COMEÇOU GEN2')
    if gen is not None:
      yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')



g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for n in g1:
    print(n)
print()

for n in g2:
    print(n)
print(n)

for n in g3:
    print(n)
print()