# Introdução às funções (def) em Python
# Funções são trechos de código usados pra replicar determinada ação 
# ao longo do seu código.
# Elas podem receber valores para parâmetros (argumentos)
# e retornar um valor específico.
# Por padrão, funções Python retornam None.

def imprimir(a, b, c):
    print(a, b, c)
    # print('Várias2')
    # print('Várias3')
    # print('Várias4s')

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Maria')
saudacao('Luiz')
saudacao()