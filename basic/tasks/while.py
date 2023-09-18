# Iterar uma string, ex: H*e*n*r*i*q*u*e

word = 'HotWheels'
index = 0
new_word = ''

while index < len(word):
    letter = word[index]
    new_word += f'*{letter}'
    index += 1 
    
new_word += '*'
print(new_word)