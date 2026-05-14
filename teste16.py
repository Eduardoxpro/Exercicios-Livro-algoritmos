# crie um programa que leia um número real qualquer pelo telcado e mostre na tela sua porção inteira
# Ex: digite um número: 6.127, O número 6.127 tem a parte inteira 6.

import math

num = float(input("Digite um número real: "))
numinteira = math.trunc(num)
print("A parte inteira do numero real: {} é: {}" .format(num, numinteira))
