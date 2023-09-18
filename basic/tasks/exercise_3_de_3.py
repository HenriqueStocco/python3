"""
Faça  um programa que peça o primeiro nome do usuário.Se o nome tiver 4 letras ou menos, seu nome é curto ; se tiver entre 5 - 6 letras -> seu nome é normal, maior que6 -> Seu nome é muito grande. 
"""

nome = input('Digíte seu nome: ').lower()
comprimento_nome = len(nome)

if comprimento_nome <= 4:
    comprimento_nome = nome
    print('Seu nome é CURTO')

elif comprimento_nome >= 5 and comprimento_nome <= 6:
    comprimento_nome = nome
    print('Seu nome é NORMAL')

elif comprimento_nome > 6:
    comprimento_nome = nome
    print('Seu nome é muito GRANDE')

else:
    print('isso é um número')
