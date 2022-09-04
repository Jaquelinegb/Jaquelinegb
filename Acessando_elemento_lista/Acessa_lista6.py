"""
Programa acessa_lista
Requisitos: Acessar elementos de uma lista com os números 1,4,7.
Autora: Jaqueline
Data: 01/09/2022
Versão: 0.0.6- introduz a estrutura de controle de fluxo for com range
"""

# Entrada de dados

lista = [1,4,7]


# Processamento de dados

# Saída de dados


for i in list(range(3)):
    print(f"O elemento {i + 1} da lista é {lista[i]}")
