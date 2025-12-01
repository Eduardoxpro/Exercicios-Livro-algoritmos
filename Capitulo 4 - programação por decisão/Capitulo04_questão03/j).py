# j) Crie um programa que leia um número inteiro positivo N
# e em seguida leia N números quaisquer (podendo ser positivos ou negativos).
# Ao final, o programa deve imprimir a quantidade de números negativos digitados.

N = int(input("Quantos números você vai digitar? "))

negativos = 0
for i in range(N):
    num = float(input(f"Digite o {i+1}º número: "))
    if num < 0:
        negativos += 1

print(f"Foram digitados {negativos} número(s) negativo(s).")
