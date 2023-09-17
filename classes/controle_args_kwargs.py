# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# Antes da barra, nenhum argumento nomeado que você passar
# na chamada da função vai funcionar, irá apresentar um erro (TypeError)
# Argumentos Posicionais devem ser antes da barra
# *args e **kwargs devem ser depois da barra

# Syntax: def f_name(positional / *args, **kwargs)
# * limita a quantidade de argumentos nomeados
# Tudo que vier antes do * deve ser positional
# Tudo que vier depois deve ser argumento nomeado

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')