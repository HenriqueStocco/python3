# Singleton -> Só pode existir uma instância de alguma coisa
# no programa todo, enquanto ele está sendo executado.
# Não é comum recarregar um módulo que ja está sendo usado
# Mas, caso queira fazer isso:
import importlib

import recarregando_modulos_m

for i in range(10):
  importlib.reload(recarregando_modulos_m)
  print(i)
  
print('Fim')