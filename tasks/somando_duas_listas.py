# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados

# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.

# Exemplo:
# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]

# ================== resultado
# lista_soma = [2, 4, 6, 8]

# Minha solução funciona apenas no Python
def zipper(lista_1, lista_2):
    limite = min(len(lista_1), len(lista_2))
    lista_soma = [(lista_1[i] + lista_2[i]) for i in range(limite)]
    return lista_soma

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
print(zipper(lista_a, lista_b))

# Solução Miranda, fuciona em qualquer langs
lista_soma = []

for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)

# Solução Miranda mais Pythônica, primeira solução
# _ é para não retornar uma tuple e valor, quero apenas o índice
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)

# Solução Miranda. segunda solução (A MELHOR)
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

# Mostrando o que está acontecendo no zip
print(list(zip(lista_a, lista_b)))
print(lista_soma)

# O zip só une as listas até o tamanho da menor lista
# Uma outra possibilidade é usar  o zip_longest para capturar os valores
# da lista maior.
from itertools import zip_longest

lista_soma_maior = [
    x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)
]

print(lista_soma_maior)

# Usamos o 'fillvalue' como 0, assim conseguimos capturar os valores
# restantes da lista maior, realizando contas, sem obter um erro.