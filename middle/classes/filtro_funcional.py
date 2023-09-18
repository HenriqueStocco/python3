# filter é um filtro funcional
# Syntax filter() - filter(function, iterator)
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

# novos_produtos = [produto for produto in produtos if produto['preco'] > 100]
novos_produtos = filter(lambda produto: produto['preco'] >= 100, produtos)
printi(produtos)
printi(novos_produtos)