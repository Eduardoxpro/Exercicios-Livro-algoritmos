A = int(input("Digite A: "))
B = int(input("Digite B: "))
C = int(input("Digite C: "))
D = int(input("Digite D: "))
E = int(input("Digite E: "))

maior = A
menor = A

for valor in [B, C, D, E]:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior Valor: {maior}")
print(f"Menor Valor: {menor}")
