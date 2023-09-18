# Criar um script que receba dois valores(não importa o tipo) e compare-os para ver qual é maior

primeiro_valor = float(input('Enter a value: '))
segundo_valor = float(input('Enter another value: '))

maior_menor = ((f'O Primeiro valor = {primeiro_valor:,.1f} é MAIOR') if (primeiro_valor > segundo_valor) else (f'O Segundo valor = {segundo_valor:,.1f} é MAIOR'))

print(maior_menor)