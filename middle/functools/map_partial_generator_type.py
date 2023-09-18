# map - para mapear dados
# Syntax func map() - map(function, iterator)
# Para coisas pequenas, apenas uma lambda já é suficiente
# partial - uma função que recebe uma função, um dos argumentos dessa função
# (ou vários argumentos) 
from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)


aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

# novos_produtos = [
#     {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}
#     for produto in produtos]
def muda_preco_produtos(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

# Para não esgotar, posso definir como lista direto no map
# Ela não irá esgotar
novos_produtos = list(map(muda_preco_produtos, produtos))

print_iter(produtos)
print_iter(novos_produtos)
# Se eu fizer isso, eu esgoto o iterator
print(list(novos_produtos)) # >>>> []

print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
print(isinstance(novos_produtos, GeneratorType)) # verifica se é um Generator

# Para listas menores, usar lambda
# Para não esgotar o iterator, usar list() antes do map()
print(list(map(lambda x: x * 3, [1, 2, 3, 4])))