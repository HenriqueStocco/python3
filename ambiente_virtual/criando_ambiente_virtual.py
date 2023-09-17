# Criando um Ambiente Virtual (Virtual Environment -> venv)
# python -m venv venv
# -m executa uma lib built-in do Python como script
# Essa lib é o venv, -m executa venv como script
# O segundo venv é o nome do Virtual Environment

# DENTRO DA PASTA VENV
# Tudo que for instalado de terceiros, irá para a pasta Lib
# Todos os executáveis que serão utilizados no ambiente virtual
# estará/irá para a pasta Scripts.
# Para sistemas Unix(Linux e Mac), a pasta bin é a mesma que a pasta Scripts

# NO POWERSHELL
# Código para ver onde o Python está instalado, o PATH
# gmc python.exe
# Caso não apareça completamente o caminho, usar:
# gmc python.exe -Syntax
# python -V, mostra a versão do Python

# OBSERVAÇÕES
# No Windows, o ExecutionPolicy é Restricted
# Isso impede a ativação de um ambiente virtual
# Para solucionar:
# Executar PowerShell como administrator
# Commands:
# Get-ExecutionPolicy Unrestricted -Force
# Antes da ativação ele pergunta se quer ativar (Recommended)
# Get-ExecutionPolicy AllSigned -Force
# Libera tudo