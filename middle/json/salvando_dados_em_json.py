# JSON - JavaScript Object Notation
# dump - jogar dados em um arquivo json
# ensure_ascii=False - vai mostrar as palavras, sem caracteres da tabela ascii
# indent=2 - deixa organizado, quebrando linha
# Salvar apenas dados simples, ele não suporta mais que isso
# É possível criar uma 'pequena' base de dados, ex: finanças pessoais
import json

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula_json.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

with open('aula_json.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])