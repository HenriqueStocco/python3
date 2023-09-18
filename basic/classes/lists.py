# CRUD com listas
# C-Create R-Read U-Update D-Delete
# evitar reescrever itens de uma lista muito grandes

lista = [10, 20, 30, 40]

lista[2] = 300
del lista[2]
print(lista)
print(lista[2])

lista_b = ['Henrique', 'Helena', 'Robson']
for nome in lista_b:
    print(nome, type(nome))