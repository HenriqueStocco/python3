# raise - lançando exceções (erros)
# PROGRAMADORES GOSTAM DOS ERROS - Flávio Miranda
# Erro é lançado quando não há mais o que fazer
# Não criar funções que vão fazer além do que ela preisa fazer
# EX: uma função que vai dividir não pode ser usada para tratar erros
# Temos que criar uma função só para tratar os erros - Zen Mode of Python

# print(123)
# raise ValueError('Deu erro')
# print(456)

# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         print('_____')
#         raise

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Cannot divide by Zero') # Erro é lançado se "d" for 
# igual 0
    return True # Se não, retorne True

def deve_ser_int_float(n):
    tipo_n = type(n) # Mostra o tipo do param "n"
    if not isinstance(n, (float, int)): # Se não "n" não for float nem int
        raise TypeError( # Lance o erro e mostre o nome do tipo de "n"
            f'"{n}" deve ser int ou float'
            f'"{tipo_n.__name__}" Enviado'
            )
    
    return True # Se "n" for int ou float, retorne True
    
def divide(n, d): # Função que divide 
    nao_aceito_zero(d) # Trata o erro ser "d" for = 0
    deve_ser_int_float(n) # Trata se "n" não for int ou float
    deve_ser_int_float(d) # Trata se "d" não for int ou float

    return n / d # Se tudo funcionar, retorne a divisão 

print(divide(8, 2))