# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

# Minha solução
my_number = 10

def double(number):
    return number*2


def triples(number):
    return number*3


def quadruples(number):
    return number*4


def operator(function):
    return function


double_number_1 = operator(double)
triple_number_1 = operator(triples)
quadruple_number_1 = operator(quadruples)
print(double_number_1(my_number))
print(triple_number_1(my_number))
print(quadruple_number_1(my_number))


# Outra solução
def create_multiplied(multiplier):
    def multiply(number):
        return number*multiplier
    return multiply


double_number_2 = create_multiplied(2)
triple_number_2 = create_multiplied(3)
quadruple_number_2 = create_multiplied(4)
print(double_number_2(2))
print(triple_number_2(3))
print(quadruple_number_2(4))