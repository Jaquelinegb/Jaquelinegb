"""
Programa soma
Descrição:
Estre programa soma dois números dados pelo usuário e imprime
na tela o resultado com uma frase explicativa.
Autor: Jaqueline Giuliani Baldissera
Verão: 0.0.3 código com erro
Data: 09/08/2022
"""

# Entrada de dados

# input é uma função que permite fa\er a leitura do teclado do usuário
# durante a execução do programa
numero_1 = input("Entre a primeira parcela.")



numero_2 = input("Entre a segunda parcela.")

# Processamento de dados

soma = numero_1 + numero_2

# Saída de dados
 # f-string
print(f"O resultado da soma do {numero_1} com o {numero_2} é igual a {soma}.")
