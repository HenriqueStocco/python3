# Decoradores são "Syntax Sugar"

def criar_funcao(funcao):
    
    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('OK, agora você foi decorada!')
        return resultado
    
    return interna

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(parametro):
    if not isinstance(parametro, str):
      raise TypeError('Parâmetro deve ser uma string')
    

invertida = inverte_string('1234')
print(invertida)