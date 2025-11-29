# c) Média de 4 notas com aprovação/reprovação
print("Digite as 4 notas bimestrais do aluno:")
N1 = float(input("Nota 1: "))
N2 = float(input("Nota 2: "))
N3 = float(input("Nota 3: "))
N4 = float(input("Nota 4: "))

MD = (N1 + N2 + N3 + N4) / 4

if MD >= 5:
    print("Aprovado")
else:
    print("Reprovado")

print(f"Média final: {MD:.2f}")
