# enumerate - enumera iteráveis (índices)
# quando usar o enumerate, usar direto no for, não criar uma var
# ou criar uma variável definindo que ela seja uma list()
#start="" de onde vai começar 

lista = ['Maria', ' Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)

lista_enum = list(enumerate(lista, start=1)) # mudei o indice zero para 1
print(lista_enum)

for indice, nome in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for tuple_enumerada in enumerate(lista):
    print('FOR da tupla: ')
    for valor in tuple_enumerada:
        print(f'{valor} ')