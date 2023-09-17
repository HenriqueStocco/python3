# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser divido em partes menores
# - Um caso recursivo que resolve o pequeno problema 
# - Um caso base que para a recursão

# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# O fatorial (!) de um número n, representado por n!, é a multiplicação de n 
# por seus antecessores maiores ou iguais a 1. Essa operação é muito comum em 
# análise combinatória.
# https://brasilescola.uol.com.br/matematica/fatorial.htm
from sys import setrecursionlimit

setrecursionlimit(1000) # Não é recomendado mudar o limite de recursão

def recursiva(inicio=0, fim=10):
    # Caso base
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva(0, 200))
