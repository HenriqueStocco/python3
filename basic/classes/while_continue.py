# continue ignora um processo de uma condição

contador = 0

while contador <= 100:
  contador += 1

  if contador == 6:
    print('Não vou mostrar o 6')
    continue # não quero que o 6 seja imprimido, o continue pula esse número

  if contador >= 10 and contador <= 27:
    print('Não vou mostrar o', contador)
    continue  # não quero que do 10 ao 27 seja imprimido, o continue pula esses números

  print(contador)
  
  if contador == 40:
    break # quando chegar a 40 ele para o while, ou, o while False

print('Acabou')
