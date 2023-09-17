# dir, hasattr, getattr em python
string = 'Henrique'
metodo1 = 'upper'
metodo2 = 'lower'
# dir -> todos os atributos que estão definidos dentro da string
print(dir(string))

# hasattr -> Checa se determinado objeto tem um determinado método
if hasattr(string, metodo1):
    print(f'Existe o método {metodo1}')
    print(string.upper())
else:
    print(f'Não existe upper')

# getattr -> Posso salvar o nome do método em uma string e verificar se existe
# o método, existindo então, eu o uso
if hasattr(string, metodo2):
    print(f'Existe o método {metodo2}')
    print(getattr(string, metodo2))
else:
    print(f'Não existe o método {metodo2}')