from sys import getsizeof as gso

# Diferença entre iterable e generator
# Iterable -> salva todos os valores na memória
# Generator -> não salva todos os valores na memória, espera pedir um valor
# Para ENORMES quantidades de dados, usar generator
# Vantagens da lista -> posso acessar índices dela
# Desvantagens de Generator -> não possui index
# porque não está salvo na memória

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]

quanto_ocupa_memoria_iterable = gso(lista)
print(quanto_ocupa_memoria_iterable)
quanto_ocupa_memoria_generator = gso(generator)
print(quanto_ocupa_memoria_generator)

print(next(generator)) # 0
print(next(generator)) # 1