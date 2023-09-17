# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys
# sys.exit() sai do programa, tudo depois dele não executará
# mostra_meu_kernel = sys.platform
# print(mostra_meu_kernel)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# print(platform)
# print(exit())

# alias 1 - import nome_modulo as apelido

# import sys as s

# sys = 'Alguma coisa'
# print(s.platform)
# print(sys)

# alias 2 - from nome_modulo import objeto as apelido

# from sys import platform as pf, exit as ex

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import *

print(platform)
exit()