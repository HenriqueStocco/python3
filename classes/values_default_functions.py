# Argumentos nomeados e não nomeados em funções Python
# Argumento nomeado tem nome com sinal de igual -> (nome=)
# Argumento não nomeado recebe apenas o argumento (nome)

# Definição da função
def soma(x, y, z):
    print(f'{x=} y={y} {z}', '|', 'x + y + z =', x + y + z)

# Execução da função ou chamada
soma(1, 2, 3)
soma(1, y=2, z=3)

print(1, 2, 3, sep='-')