from os import remove, unlink, rename
arquivo = 'C:\\Users\\henri\\Documents\\vscode\\python\learning\\cursos_python\\flavio_miranda\\intermediario\\'
arquivo += 'test.txt'

with open(arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Olá, Mundo!')
    arquivo.write('Olá, Mundo!')
    arquivo.write('Olá, Mundo!')


# Renomeando o arquivo
rename(arquivo, 'text.txt')
# Tanto remove quando unlink apagam(excluem) o arquivo
remove(arquivo)
# unlink(arquivo)