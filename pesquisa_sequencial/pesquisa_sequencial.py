"""
Programa pesquisa_sequencial
Requisitos: Este programa procura um elemente dentro de uma lista PYthon.
Autora: Jaqueline
Data: 01/09/2022
Versão: 0.0.1
"""

# Entrada
L = [1, 2, 3, 7, 8, 9]

numero = int(input("/nDigite o número a procurar:"))

encontrado = False

# Processamento
indice = 0

while indice < len(L):
    if L[indice] == numero:
        encontrado = True
        break
    indice +=1
    
# Saída
if encontrado:
    print(f"\no valor {numero} foi encontrado na posição {indice}.")
else:
    print(f"\no valor {numero} fnão foi encontrado.")
