# Arquivos que são criados para importar em outro
# São chamados de modules (módulos)
# Pastas que vão conter funcionalidades que serão importadas em outro lugar
# São chamados de Packages (pacotes)

# from sys import path as p
# print(__name__)
# print(*p, sep='\n')

# 3 formas de importar um módulo e usá-lo
import package_aula.module
print(package_aula.module.soma(2, 2))

from package_aula import module
print(package_aula.module.soma(3, 3))

from package_aula.module import soma
print(module.soma(4, 4))

from package_aula.module import * # Má prática, não usar
print(variavel_1)