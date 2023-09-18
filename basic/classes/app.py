from module import sum

print(__name__) # Me mostra se eu estou executando o arquivo em que estou, ou se estou executando um externo,um modulo
# Para arquivo em que estou: imprime __main__
# Para externo: imprime o nome do externo

print(sum(10, 30))
