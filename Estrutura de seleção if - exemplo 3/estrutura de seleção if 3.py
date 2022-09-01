"""
Estrutura de seleção if: exemplo 3
Descrição:
#Faça um programa que pergunte a idade de uma pessoa
#Se a idade for 13 anos, imprima na tela
#"Oi! Voce eh uma criança."
#Se a idade for de 13 a 17 imprima
#"Oi, voce eh um adolescente."
#Se a idade for maior que 17 anos imprima
"Oi! Voce eh um adulto."

Autor: Jaqueline Giuliani Baldissera
Data: 29/08/2022
"""

# Entrada de dados

idade = int(input("Qual a sua idade?"))


# Processamento e saida de dados
if idade < 13:
    print("Oi! Voce eh uma crianca.")
elif idade >= 13 or idade <= 17:
    print("Oi, Voce eh um adolescente.")
else:
    print("Voce eh adulto.")
