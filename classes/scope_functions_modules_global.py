# Escopo de funções em Python.
# Escopo significa o local onde aquele código pode atingir.
# Existe o escopo global e local.
# Local -> é o escopo onde apenas nomes do mesmo local podem ser alcançados.
# Global -> em todo o código é alcançavel.

x =1 

def scope():
    global x
    x = 10

    def another_function():
        x = 11
        y = 2
        print(x, y)
        
    another_function()
    print(x)


print(x)
scope()
print(x)