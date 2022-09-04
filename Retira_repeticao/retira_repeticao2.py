"""
Programa retira_repeticao
Requisitos: Dada uma lista de dados do usuário, retire todos os dados repetidos.
Coloque na tela a lista sem repetição.
Autora: Jaqueline
Data: 01/09/2022
Versão: 0.0.1
"""

# Entrada
# Leitura do teclado do usuário
lista = []

while True:
    elemento = input("\nDigite um elemento da sua lista. Ou, digite X para encerrar.")
    if elemento.upper() == "X":
        break
    lista.append(elemento)

        
# Processamento
# Retire todos os dados repetidos
for i in list(range(len(lista) + 1)):
    for j in list(range(len(lista) + 1)):
        if lista[j] == lista[j + 1]:
            del lista[j+ 1]


# Saída
# Colocar na tela e lista sem repetição
print("fa lista sem repetição é {lista}.")
