# Os packages podem ser inicializados com um arquivo chamado __init__.py
# Qualquer coisa que for importada dentro dele, vai ser executada
# O init faz o Python achar que o package é um módulo, importando aquelas coisas
# pra dentro do package

from package_aula import dobra

print(dobra(2))