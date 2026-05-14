# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo
import math

angle = float(input("Digite o valor do angulo em graus: "))
rad = math.radians(angle)
seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)
print("O seno é: {:.2f} em conseno é: {:.2f} a tangente é: {:.2f}" .format(seno, coseno, tangente))