"""
Programa soma
Requisitos: Este programa lê dois números digitados pelo usuário
calcula a soma deles e coloca o resultado na tela.
Autora: Jaqueline
Data: 02/09/2022
Versão: 0.9.0
"""

# Definição de funções

def entra_dados():
    """Esta função (procedimento) lê dois números digitados pelo usuário"""
    i = 0
    lista_numeros = []
    while i < 2:
        numero = float(input("\nDigite um número: "))
        lista_numeros.append(numero)
        i+=1
    return lista_numeros

