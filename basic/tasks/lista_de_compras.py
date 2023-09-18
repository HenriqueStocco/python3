"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar  e listar
valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista

inserir[i], apagar[a], listar[l]
"""
# SOLUÇÃO DO MIRANDA
from os import system as sys

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if opcao == 'i':
        sys('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digíte número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')

    elif opcao == 'l':
        sys('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    elif opcao == 's':
        sys('cls')
        print('Até mais.')
        break