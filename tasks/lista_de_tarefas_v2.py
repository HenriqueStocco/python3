# Função listar foi embutida nas funções devido
# a complexidade da lógica

from os import system as sys

tarefas = []
tarefas_refazer = []

def listar(tarefas):
    print()
    if not tarefas: 
        print('Nenhuma Tarefa para Listar')
        print()
        return
    
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
        return
    
    tarefas.append(tarefa)
    print(f'{tarefa=} foi adicionada à lista de tarefas')
    print()
    listar(tarefas)


while True:
    # Nesse caso, sem a lambda, ele executará todas as funções, e o return None
    # Para adiar a execução dessas funções
    # Apenas é preciso envolver elas em outra função
    # lambda: sem parâmetro está adiando as funções
    comandos = {
            # 'listar': lambda: listar(tarefas),
            'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
            'refazer': lambda: refazer(tarefas, tarefas_refazer),
            'limpar': lambda: sys('cls'),
            'adicionar': lambda: adicionar(tarefa, tarefas),     
    }
    
    print('Comandos: listar, desfazer, refazer, limpar(terminal)')
    tarefa = input('Digíte uma tarefa ou comando: ')

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
    comandos['adicionar']
    comando()