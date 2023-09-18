# Generator expression, Iterables e Iterators em Python
# O iterável possui os valores
# o Iterador mostra esses valores, um por vez
# Iterator não sabe o tamanho, o anterior e nem nada
# Apenas mostra sabe o próximo

iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))