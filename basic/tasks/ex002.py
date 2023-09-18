"""Peça para digitar o nome, idade, se o nome e a idade forem digitados exiba:
- nome, nome invertido, se contém espaços ou não, quantas letras tem o nome, primeira letra, última letra.
Se não for digitado, exiba:
- desculpe, nome e idade não foram digitados
"""

nome = input('Enter your name: ').strip().capitalize()
idade = input('Enter your age: ').strip()

if nome and idade:
  print(f'Seu nome é {nome}')
  print(f'Seu nome invertido é {nome[-1::-1]}')
  print(f'Seu nome {nome} Contém espaços' if ' ' in nome else f'Seu nome {nome} Não contém espaços')
  print(f'Seu nome tem {len(nome)} letras')
  print(f'A primeira letra do seu nome é {nome[0]}')
  print(f'A última letra do seu nome é {nome[-1]}')
else:
  print('Desculpe, nome e idade não foram digitados')