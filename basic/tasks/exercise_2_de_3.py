"""
Faça um programa que pergunte a hora ao usuário e, baseando-se  no horário descrito, exiba a saudação apropriada:
Bom dia 0-11, boa tarde 12-17, boa noite 18-23
"""

horario_atual = input('Digite o horário atual: ')

if horario_atual.isdigit():
  horario_atual = int(horario_atual)

  if horario_atual >= 0 and horario_atual <= 11:
    print('Bom Dia, está um lindo dia hoje!')

  elif horario_atual >= 12 and horario_atual <= 17:
    print('Boa Tarde, tenha uma ótima tarde!')

  elif horario_atual >= 18 and horario_atual <= 23:
    print('Boa Noite, tenha um bom descanso!')
else:
  print('Isso não é um horário')

"""
RESOLUÇÃO DO MIRANDA:

entrada = input('Digíte a hora em números inteiros: ')

try:
  hora = int(entrada)
s
  if hora >= 0 and hora <= 11:
    print('Bom dia')

  elif hora >= 12 and hora <= 17:
    print('Boa tarde')

  elif hora >= 18 and hora <= 23
    print('Boa noite')

  else:
    print('Não conheço essa hora')

execpt:
  print('Por favor, digite apenas números inteiros')
"""