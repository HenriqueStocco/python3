# Problema dos parâmetros mutáveis em funções Python
# Se eu chamar a função sem passar o parâmetro, o Python vai usar a mesma lista
# Para eu adicionar em outra lista, eu tenho que passar(criar) outra lista
# Forma ideal é não passar parâmetros mutáveis em argumentos padrão da função
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


# Forma simples de resolver
lista_1 = []

cliente_1 = adiciona_clientes('Luiz', lista_1)
adiciona_clientes('Joana', cliente_1)
adiciona_clientes('Fernando', cliente_1)
cliente_1.append('Edu')
print(cliente_1)

cliente_2 = adiciona_clientes('Helena')
adiciona_clientes('João', cliente_2)
print(cliente_2)

cliente_3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente_3)
print(cliente_3)