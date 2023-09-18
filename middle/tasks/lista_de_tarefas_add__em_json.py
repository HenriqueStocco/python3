import os 
import json 

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


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(
            tarefas, arquivo, indent=2, ensure_ascii=False
            )


CAMINHO_ARQUIVO = 'lista_de_tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    comandos = {
            'adicionar': lambda: adicionar(tarefa, tarefas),
            'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
            'refazer': lambda: refazer(tarefas, tarefas_refazer),
            'limpar': lambda: os.system('cls'),
    }

    print('Comandos: listar, desfazer, refazer, limpar(terminal)')
    tarefa = input('Digíte uma tarefa ou comando: ')    

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
    comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)