"""
Estrutura de seleção if: exemplo 1
Descrição:
#Faça um programa que pergunte a idade de uma pessoa
#Se a idade for maior do que 18 anos, o programa imprime na tela o texto
# "Oi! Você é um adulto."
Autor: Jaqueline Giuliani Baldissera
Data: 29/08/2022
"""

# Entrada de dados

idade = int(input("Qual a sua idade?"))


# Processamento e saida de dados
if idade > 18:
    print("Oi! Voce eh um adulto.")
else:
    print("Oi! voce eh menor de idade.")
