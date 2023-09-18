# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# Minha tentativa da Solução
# lista_de_tarefas = []

# while True:
#   print('Comandos: listar, desfazer, refazer')
#   adicionar_tarefa = input('Digíte uma Tarefa ou um Comando: ').lower()
#   print()
#   tarefas = ''

#   if adicionar_tarefa == 'listar':
#     if len(lista_de_tarefas) == 0:
#       print('Nada para Listar')

#     else:
#       for tarefa in lista_de_tarefas:
#         print(tarefa)
#     print()

#   elif adicionar_tarefa == 'desfazer':
#       if len(lista_de_tarefas) == 0:
#         print('Nada para Desfazer')

#       else:
#         tarefas_desfeitas = []
#         tarefas_desfeitas.append(lista_de_tarefas[-1]) 
#         del lista_de_tarefas[-1]
  
#   elif adicionar_tarefa == 'refazer':
#     lista_de_tarefas.append(tarefas_desfeitas[-1])
#     del tarefas_desfeitas[-1]

#   elif adicionar_tarefa:
#     tarefas = adicionar_tarefa
#     lista_de_tarefas.append(adicionar_tarefa)


# Solução do Miranda
from os import system as sys

tarefas = []
tarefas_refazer = []

def listar(tarefas):
    print()
    if not tarefas: # Esse tipo de condicional é chamado de Guard Clause
        print('Nenhuma Tarefa para Listar')
        print()
        return # Esse return dentro do if para a execução da função
    
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nada para Desfazer')
        print()
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa =} foi removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma Tarefa para Refazer')
        print()
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} foi adicionada à lista de tarefas')
    print()
    tarefas.append(tarefa)
    print()
    listar(tarefas)

    
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nenhuma Tarefa foi Digitada')
        print()
        return # Esse return dentro do if para a execução da função
    
    tarefas.append(tarefa)
    print(f'{tarefa=} foi adicionada à lista de tarefas')
    print()


while True:
    print('Comandos: listar, desfazer, refazer, limpar(terminal)')
    tarefa = input('Digíte uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    
    elif tarefa == 'limpar':
        sys('cls')
        continue
    
    else:
        adicionar(tarefa, tarefas)
        continue
    