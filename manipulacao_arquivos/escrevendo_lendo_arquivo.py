# Como o arquivo está na mesma pasta, não preciso do caminho completo
# Tanto path\\path como o r'path\path' funcionam
caminho_arquivo = 'test.txt'

# com w+ consigo ler escrever no(o) arquivo
with open(caminho_arquivo, 'w+') as arquivo:
    # É necessário \n para quebrar a linha
    # Ou \r\n
    print(type(arquivo)) # Python module '_io.TextIOWrapper'
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    # Consigo escrever várias linhas
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4')
        )
    # Move o cursor para a primeira linha, no começo
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print('READLINES')
    for linha in arquivo.readlines():
        print(linha.strip())

    # print('Arquivo foi Fechado!')
print('#' * 10)
# Se eu abrir novamente o arquivo, não preciso cria-lo
# Apenas ler ele
with open(caminho_arquivo, 'r') as arquivo:
    # arquivo.read() # Lê o arquivo inteiro
    print(arquivo.read())
