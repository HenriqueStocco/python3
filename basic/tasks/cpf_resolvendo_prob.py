"""
Resolvendo possíveis problemas do validador de cpfs
- problemas com caracteres
"""

# replace() substitui os especificados, ex: ., -, etc
# replace fuciona assim:.replace('oq substituir', 'para oq substituir')
# substituindo simbolos para nada
cpf = '746.824.890-70'.replace('.', '').replace(' ', '').replace('-','')
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