# Criando arquivos com Python
# Usamos a função open para abrir um arquivo em Python
# (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis:
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre módulos os, mas:
# os.remove  ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump - Gera arquivo json
# json.load
caminho_completo = 'C:\\Users\\henri\\Documents\\vscode\\python\learning\\cursos_python\\flavio_miranda\\intermediario\\'
caminho_completo += 'test.txt' 
# arquivo = open(caminho_completo, 'w')
# # Sempre fechar o arquivo
# arquivo.close()

# Dessa forma o arquivo vai ser aberto, vai executar o que precisa e
# vai fechar automaticamente
with open(caminho_completo, 'w') as arquivo:
    print('Olá, Mundo!')
    print('Arquivo vai ser fechado.')