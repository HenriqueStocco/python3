# finally sempre será executado, mesmo que ocorra um erro.

# ex: Você quer abrir um arquivo, mas no meio do processo ocorre um erro
# e o arquivo fica aberto
# Você pode usar o finally para fechar o arquivo
# doc exceptions https://docs.python.org/3/library/exceptions.html

try: 
    print('ABRIR ARQUIVO')
    8/0 # Apenas para gerar o erro

except ZeroDivisionError as e: # Tratando o erro
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
    
except IndexError as error:
    print('IndexError')

except (NameError, ImportError):
    print('NameError, ImportError')

else:
    print('Não deu certo')
    
finally: # Executa sempre
    print('FECHAR ARQUIVO')