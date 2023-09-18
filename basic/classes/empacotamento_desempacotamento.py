"""
Introdução ao desempacotamento + tuples()
"""
#nomes = ['Maria', 'Helena', 'Luiz']
# ter a mesma quantidade de valor e variável
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

nome1, *_ = ['Maria', 'Helena', 'Luiz'] # desempacota o nome1['Maria']
# e empacota o resto que não vai ser o resto

_, nome2, *_ =  ['Maria', 'Helena', 'Luiz']

print(nome1)
print(nome2)