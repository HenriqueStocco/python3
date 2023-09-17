# Evitando condicionais
# Guard Clause -> Inverter a lógica do if e não usar o else

# Exemplo de Guard Clause:
# Normal(evitar isso, quando possível)
def f_sem_guarda(x):
    if isinstance(x, int):
# return por padrão ja retorna None se a condição não for verdadeira
        return x + 1
    else: # Essa condição está inútil
        return None
    

# Guard Clause(usar sempre que puder)
# Invertendo a lógica do if, diminui linha e processamento do código
# Fica simples de ler, e não tem partes inúteis
def f_com_guarda(x):
    if not isinstance(x, int):
        return None
    
    return x + 1

