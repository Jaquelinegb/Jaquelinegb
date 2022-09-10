"""Importação de módulos
Descrição: 
Este módulo importa o módulo de entrada_saida e o módulo aritmético.
Autora: Jaqueline
Data:09/09/2022
Versão: 1.0.0"""

# Importação de módulo

import aritmetico
import entrada_saida

# Definição de funções

def main():
    lista_numeros = entrada_saida.entrada()
    operacao = input("""Qual operação você deseja?  Digite:
             + para adição,
             - para subtração,
             x - para multiplicação ou
             / para divisão\n""")
    
    if operacao == "+":
        valor = aritmetico.adicao(lista_numeros[0], lista_numeros[1])
    elif operacao == "-":
        valor = aritmetico.subtracao(lista_numeros[0], lista_numeros[1])
    elif operacao == "x":
        valor = aritmetico.multiplicacao(lista_numeros[0], lista_numeros[1])
    elif operacao == "/":
        valor = aritmetico.divisao(lista_numeros[0], lista_numeros[1])
    else:
        valor = "Esta operação não está definida para esta calculadora."
    entrada_saida.saida(valor)

if __name__ == "__main__":
    main()
