# High order function
# Funções de primeira classe

def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(func, *msg): # Executa -> saudacao(msg, nome e um pouco mais)
    return func(*msg)


#saudacao_1 = executa(saudacao, 'Boa Noite!') Aponta uma variável para uma
# função, ou a mesma função
print(executa(saudacao, 'Bom Dia!', 'Luiz'))
print(executa(saudacao, 'Boa Noite!', 'Maria'))