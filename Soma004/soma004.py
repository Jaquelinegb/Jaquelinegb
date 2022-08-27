"""
Programa soma
Descrição:
Estre programa soma dois números dados pelo programador e imprime
na tela o resultado com uma frase explicativa.
Autor: Jaqueline Giuliani Baldissera
Verão: 0.0.4 
Data: 09/08/2022
"""

# Entrada de dados

#input é uma função que permite fazer a leitura do teclado do usuário
#durante a execução do programa
numero_1 = float(input("Entre a primeira parcela."))



numero_2 = float(input("Entre a segunda parcela."))

# Processamento de dados

soma = numero_1 + numero_2

# Saída de dados

# f-string

print(f"O resultado da soma do (número_1) com o (número_2) é igual a {soma}.")
