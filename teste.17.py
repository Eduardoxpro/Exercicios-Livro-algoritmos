#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# rentangulo. calcule e mostre o comprimento da hipotenusa.
import math

cateto_oposto = int(input("Digite o cateto oposto de um triângulo rentangulo: "))
cateto_adjacente = int(input("Digite o cateto adjacente de um triangulo retangulo: "))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
print("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa) )