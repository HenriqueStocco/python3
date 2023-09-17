# Free vars + nonlocal (locals, globals)

# def fora(x):
#     a = x

#     def dentro():
#       print(locals()) # Mostra a variável livre e o valor dela
#       return a # Essa é uma variável livre porque ela não foi declarada
#     # no escopo da função dentro
#       print(dentro.__code__.co_freevars) # esse linha mostra as variáveis 
#       # livres
#     return dentro


# dentro_1 = fora(10)
# dentro_2 = fora(20)
# print(dentro_1())
# print(dentro_2())

# Eu não posso modificar ou usar a variável livre em outro escopo
# apenas pegar seu valor
# nonlocal não é nem local e nem global
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)