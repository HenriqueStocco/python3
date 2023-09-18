# Exercício - Unir Listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
# No caso, tanto a função zipper(criada) como a zip(Python), usam o valor da
# lista menor
# E zip_longest usa o valor da lista maior

# Criando a função zip do Python
# def zipper(lista_1, lista_2):
#     intervalo = min(len(lista_1), len(lista_2))
#     return [(lista_1[i], lista_2[i]) for i in range(intervalo)]

# lista_nomes_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista_abreviacoes_nomes_cidades = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(lista_nomes_cidades, lista_abreviacoes_nomes_cidades))

from itertools import zip_longest

lista_nomes_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_abreviacoes_nomes_cidades = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista_nomes_cidades, lista_abreviacoes_nomes_cidades)))
# Nesse caso eu teria que usar um fillvalue=''
# Porque a lista de abreviacoes possui um índice a mais
# caso eu não use o fillvelue='', a lista ficará assim: [..., (None, 'RJ')]
print(
    list(zip_longest(
        lista_nomes_cidades, lista_abreviacoes_nomes_cidades, 
        fillvalue='SEM CIDADE')))
