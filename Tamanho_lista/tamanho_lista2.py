"""
Programa tamanho_lista
Requisitos: Este programa calcula o tamanho de uma lista Python dada pelo usuário
e o coloca na tela.
Autora: Jaqueline
Data: 01/09/2022
Versão: 0.0.1
"""

# Entrada de dados
# entrada do usuário pelo teclado

lista = []
while True:
    elemento = input("/nDigite um elemento para sua lista. Quando encerrar, digite X e pressione ENTER.  ")
    if elemento == "X":
        break
    lista.append(elemento)


# Processamento de dados
#calcula o tamanho de uma lista Python
tamanho_lista = len(lista)


# Saída de dados
#coloca o tamanho da lista na tela.

print(f"A lista digitada foi{lista} e seu tamanho é {tamanho_lista}.")
