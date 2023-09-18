# Como o for funciona por trás dos panos
# Iterável -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

#texto = 'Luiz'.__iter__() # mostra o objeto e o local que ele está na memória
# mesma coisa, mas com o método pronto
texto = 'Henrique'
iterador = iter(texto)

#print(texto.__next__()) imprime o próximo valor do texto
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())

#print(next(texto)) # mesma coisa, só com o método pronto

# Isso aqui é igual a ->>
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
    
# Igual a isso ->>
for letra in texto:
    print(letra)