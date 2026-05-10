A = int(input("Digite A: "))
B = int(input("Digite B: "))
C = int(input("Digite C: "))
D = int(input("Digite D: "))

for valor in [A, B, C, D]:
    if valor % 2 == 0 or valor % 3 == 0:
        print(valor)
