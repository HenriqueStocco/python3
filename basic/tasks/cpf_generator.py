from random import randint
from sys import exit

nove_digitos = ''

for i in range(9):
    nove_digitos += str(randint(0, 9))

print(nove_digitos)

exit() # para de executar os de baixo

cpf = '746.824.890-70'.replace('.', '').replace(' ', '').replace('-','')
contador_regressivo1 = 10
resultado_digito1 = 0

for digito in nove_digitos:
  resultado_digito1 += int(digito) * contador_regressivo1
  contador_regressivo1 -= 1

primeiro_digito = (resultado_digito1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

print(primeiro_digito)

dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo2 = 11
resultado_digito2 = 0

for digito in dez_digitos:
    resultado_digito2 += int(digito) * contador_regressivo2
    contador_regressivo2 -= 1

segundo_digito = (resultado_digito2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(segundo_digito)
novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == novo_cpf:
    print(f'{novo_cpf} é válido')
else:
    print('CPF inválido')