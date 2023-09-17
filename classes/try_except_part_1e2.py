# try, except parte 1 e 2
# Exceções são classes herdadas da classe principal Exception
# Forma correta de tratar erros é passando qual tipo de erro ocorreu/ pode ocorrer
# Normalmente os erros não são tratados juntos como -> (TypeError, IndexError) as error:

try: # tente executar
  a = 18
  b = 0
  print('Linha 1'[1000])
  c = a / b
  print('Linha 2')
except ZeroDivisionError: # se não conseguir, mostre o erro 
    print('Dividiu por zero.')

except NameError: # se não conseguir, mostre o erro 
    print('algum nome não está definido.')

except TypeError: # se não conseguir, mostre o erro 
    print('Erro de tipo.')

except (TypeError, IndexError) as error: # Posso tratar dois erros ao mesmo tempo,
# colocando dentro de uma tuple
    print('Erro de tipo + IndexError.')
    print('msg:', error) # Mostra qual foi o erro
    print("Nome", error.__class__.__name__) # Mostra o nome do erro ocorrido
    
except Exception: # Classe superior, trata qualquer erro e nenhum except vai executar 
# depois dele
    print('Erro desconhecido.')


print('CONTINUAR...')