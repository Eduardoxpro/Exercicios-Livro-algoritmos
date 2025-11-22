# 4.c) Calcular o volume de uma lata de óleo
import math
raio = float(input("Digite o raio da lata (em cm): "))
altura = float(input("Digite a altura da lata (em cm):"))
volume = math.pi * raio**2 * altura
print (f"c) O volume da lata é {volume:.2f} cm³")
print("="*50)