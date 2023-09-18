# 'w' e 'a' cria e escreve em(um) arquivo
# Mas existe uma diferença crucial entre eles
# O 'w' apaga o que tiver no arquivo e escreve de novo, toda vez
# o 'a' continua escrevendo na próxima linha
# Encoding - são caracteres especiais, acentuação em arquivos de texto
# Sempre colocar o encoding='utf-8' para arquivos de texto

arquivo = "test.txt"

with open(arquivo, 'w', encoding='utf-8') as archive:
    archive.write('Usando "w"\n')
    archive.write('Usando "a"\n')
    archive.write('ATENÇÃO\n')
    archive.writelines(('Linha 4\n', 'Linha 5\n'))