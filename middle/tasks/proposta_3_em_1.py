from copy import deepcopy

# Exercícios
# 1 -> Aumente os preços dos produtos a seguir em 10%
# 1.1 -> Gere novos_produtos por deep copy (cópia profunda)

# 2 -> Ordene os produtos por nome decrescente (do maior para menor)
# 2.1 -> Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# 3 -> Ordene os produtos por preco crescente (do menor para maior)
# 3.1 -> Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00}, # 11.00
    {'nome': 'Produto 1', 'preco': 22.32}, # 24.552
    {'nome': 'Produto 3', 'preco': 10.11}, # 11.120999999999999
    {'nome': 'Produto 2', 'preco': 105.87}, # 116.45700000000001
    {'nome': 'Produto 4', 'preco': 69.90}, # 76.89
]

new_products = [{**p, 'preco': round(p['preco']*1.1, 2)}  for p in deepcopy(produtos)]

product_sorted_by_name = sorted(deepcopy(produtos), key=lambda p: p['nome'], reverse=True)
product_sorted_by_price = sorted(deepcopy(produtos), key=lambda p: p['preco'])

print(*produtos, sep='\n')
print()
print(*new_products, sep='\n')
print()
print(*product_sorted_by_name, sep='\n')
print()
print(*product_sorted_by_price, sep='\n')