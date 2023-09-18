"""
CUIDADO com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'Henrique'
outra_variavel = nome
nome = 'João'
print(nome)
print(outra_variavel)

lista_a = ['Henrique', 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)