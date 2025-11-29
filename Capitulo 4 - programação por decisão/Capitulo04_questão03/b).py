# b) Valor positivo ou cálculo de média com 4 notas
N = int(input("Digite um valor inteiro (N): "))

if N >= 0:
    print(f"O valor lido é positivo: {N}")
else:
    print("Como o valor foi negativo, digite as 4 notas do aluno:")
    N1 = float(input("Digite a nota 1: "))
    N2 = float(input("Digite a nota 2: "))
    N3 = float(input("Digite a nota 3: "))
    N4 = float(input("Digite a nota 4: "))
    
    MD = (N1 + N2 + N3 + N4) / 4
    
    if MD >= 5:
        print("Aprovado")
    else:
        print("Reprovado")
    
    print(f"Média final: {MD:.2f}")
