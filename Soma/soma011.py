"""
Programa soma
Requisitos: Este programa lê dois números digitados pelo usuário
calcula a soma deles e coloca o resultado na tela.
Autora: Jaqueline
Data: 02/09/2022
Versão: 0.1.0
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


def adicao(numero_1, numero_2):
    """Esta função calcula a soma dos números numero_1 e numero_2"""
    return numero_1 + numero_2


def impressora(soma, numero_1, numero_2):
    """Esta função coloca o resultado da soma do numero_1 com o numero_2 na tela"""
    print(f"\nA soma do {numero_1} com o {numero_2} é igual a {soma}.")


def main():
    # Entrada
    entra_dados()

    # Processamento
    adição(numero_1, numero_2)


    # Saída
    impressora(soma, numero_1, numero_2)

# Execução do programa

main()

