# quando colocamos * depois de uma string, multiplica, ex: n *2 => 22
# quando colocamos + depois de uma string, concatena, ex: n + 2 => n2
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar
# sempre que o usuário me mandar alguma coisa, eu preciso tratar essa coisa


n = input('Dobrarei o número que você digitar: ')

#if n.isdigit():
#  nf = float(n)
#  print(f'O dobro de {n} é {nf*2:.2f}')
#else:
#  print('isso não é um número')

#n.isdigit()#verifica se é uma string
# if checa uma condição e muda o fluxo, mas se ocorrer um erro ele não evita o erro
# try e except trata o erro
#try: tenta executar o código
#except: se não funcionar no meu try, execeuta isso

# nome disso é FAIL FAST, queremos encontram o erro o mais rápido possível
try:
  nf = float(n)
  print('STR:', n)
  print('FLOAT:', nf)
  print(f'O dobro de {n} é {nf*2:.2f}')

except:
   print('isso não é um número')

# NÃO É MUITO PRUDENTE USAR O try E except DESSA MANEIRA