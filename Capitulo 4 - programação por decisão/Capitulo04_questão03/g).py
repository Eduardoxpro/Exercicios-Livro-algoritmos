# g) Faça um programa que leia 5 números e informe o maior número.

numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print(f"O maior número é: {max(numeros)}")
# ou sem usar max():
maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
print(f"O maior número é: {maior}")
