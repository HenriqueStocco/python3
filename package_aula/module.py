"""
Quando no meu código, eu importar all(*), só vou poder usar o que estiver
dentro do __all__, como está logo abaixo
"""

__all__ = [
    'variavel_1'
]

variavel_1 = 'Vou poder ser usada'
variavel_2 = 'Não vou ser usada'

def soma(x, y):
    return x + y