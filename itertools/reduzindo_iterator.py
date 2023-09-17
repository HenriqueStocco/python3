from functools import reduce

# reduce - faz a redução de um iterator em um valor
# Syntax reduce() - reduce(function, iterator, initial)
def printi(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# total = 0
# for produto in produtos:
#     total += produto['preco']
# print(round(total))

# total = ''
# print(sum([p['preco'] for p in produtos]))

# Usar sempre o valor inicial
# def funcao_de_reduce(acumulador, produto):
#     print('acumulador -> ', acumulador)
#     print('produto -> ', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce(
    lambda acumulador, produto: acumulador + produto['preco'], produtos, 0)
print(round(total))