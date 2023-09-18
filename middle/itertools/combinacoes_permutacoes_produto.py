# Combinations, Permutations and Products - itertools
# Combination - Ordem não importa - iterável + tamanho do grupo
# Permutation - Ordem importa
# Product - Ordem importa e repete valores únicos
# Syntax - combinations(iterator, grupo)
#          combinations(pessoas, 2) >>>> ('João', 'Joana'),('João','Luiz'),....
from itertools import combinations, product, permutations

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

pessoas = ['João', 'Joana', 'Luiz', 'Letícia',]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm','g'],
    ['male', 'female', 'unisex'],
    ['algodão', 'poliéster'],
]

# Não repete combinações, ex: ('João', 'Joana'), ('Joana', 'João')...
print_iter(combinations(pessoas, 2))
# Faz todas as combinações possíveis
print_iter(permutations(pessoas, 2))
# Desempacotando o iterator, tenho todas as combinações
print_iter(product(*camisetas))