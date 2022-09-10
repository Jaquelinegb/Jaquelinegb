"""
Descrição: Este módulo entrará com dois números e
apresentará na tela o valor
Autora: Jaqueline
Versão: 1.0.0
Data: 09/09/2022
"""


def entrada() -> list:
    
    """
    Esta instrução diz para o computador guardar o primeiro número em um endereço
    de memória e "apelidar" este endereço de num_1 e guardar o segundo número em
    um endereço de memória e "apelidar" este endereço de num_2
    """

    num_1 = float(input("\nDigite o primeiro número: "))
    num_2 = float(input("\nDigite o segundo número: ")) 
    return [num_1, num_2]


def saida(valor: float):
    
    """
    Saída de dados
    """
    print(f"\nO resultado da operação é igual a {valor}.")
