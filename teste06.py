#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

import math

VAR = int(input("Digite o valor: "))
VAR2X = VAR * 2
VAR3X = VAR * 3
raiz = math.sqrt(VAR)
print ("O dobro do valor digitado é: {}, o triplo do valor digitado é: {}, a raiz quadrada do valor digitado é: {} " .format(VAR2X, VAR3X, raiz) )