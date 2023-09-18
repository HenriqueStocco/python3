"""
Faça um programa que peça para o usuário digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não um número inteiro.
"""

numero = input('Digite um número: ')

if numero.isdigit():
    numero = int(numero)
    par_impar = (f'O número {numero} é Par' if ((numero%2) == 0) else 'O número {numero} é Ímpar')
    print(par_impar)

elif numero.isdigit():
    print(f'O número "{numero}" não é um número')

else:
    numero = float(numero)
    print(f'O número {numero:.2f} não é um Inteiro, é um Float')
