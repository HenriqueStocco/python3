# Generator são funções que pausam
# Toda função geradora usa yield
# yield pausa a execução da função e salva
# Só vai executar se usarmos next()

# def generator(n=0):
#     yield 1 # Pausar
#     #return 'ACABOU'
#     print('Continuando...')
#     yield 2 # Pausar
#     print('Continuando...')
#     yield 3
#     print('Vou terminar')
#     return 'ACABOU'

# gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Fazer tudo isso dinâmicamente
# for n in gen:
#     print(n)

# Fazendo tudo na mão
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen = generator(maximum=100)
for n in gen:
    print(n)