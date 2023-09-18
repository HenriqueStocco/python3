"""
Validando CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva
começando de 10

Ex:   746.824.890-70 (74682489070)
    10  9  8  7  6  5  4  3  2
 *  7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta

Primeiro dígito da CPF é 7
"""

"""coletando_cpf = 746823890

multiplicacao = [(10 * 7) + (9 * 4) + (8 * 6) + (7 * 8) + (6 * 2) + (5 * 4) + (4 * 8) + (3 * 9) + (2 * 0)]

for item in multiplicacao:
    continue

resto = (item * 10) % 11
print(resto)

if resto > 9 :
    print('Resultado é 0')
elif resto >= 1:
    print('É o valor da conta:', resto)
else:
    print('Sla')
"""

# Solução Miranda
# Descobrindo o primeiro dígito do cpf

cpf = '74682489070'
nove_digitos = cpf[:9] # caminha pela string, do indice 0 ao 9
contador_regressivo1 = 10 # define o valor do contador regressivo
resultado_digito1 = 0 # define o resultado como 0 para acrescentar dentro do for

for digito in nove_digitos:
# cada loop adiciona um novo valor na variável resultado que é somado com o próximo valor, assim fazendo a soma de todos os números do cpf
# digito é a variável criada no for para pegar cada índice do cpf, e convertida para int
# resultado = resultado + (7 * 10) == 0 + 70
# resultado = resultado + (4 * 9) == 70 + 36
    resultado_digito1 += int(digito) * contador_regressivo1
# cada loop o contador decrementa o valor definido, ex: loop1 = 10, loop2 = 9 ....
    contador_regressivo1 -= 1

# pega o resultado 301, multiplica por 10 - 3010 e pega o resto da divisão por 11
primeiro_digito = (resultado_digito1 * 10) % 11
# se o resto for menor ou igual a 9, é o próprio número, se for maior que 9 e menor que 1 é 0
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)

# Descobrindo o segundo dígito do cpf

# adiciona o primeiro dígito no cpf para calcular o segundo
dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo2 = 11
resultado_digito2 = 0

# mesma coisa do primeiro dígito
for digito in dez_digitos:
    resultado_digito2 += int(digito) * contador_regressivo2
    contador_regressivo2 -= 1

segundo_digito = (resultado_digito2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(segundo_digito)

# Validando o CPF
#                 cpf            7               0
novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == novo_cpf:
    print(f'{novo_cpf} é válido')
else:
    print('CPF inválido')