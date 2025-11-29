# a) Diferença do maior valor pelo menor valor
A = int(input("Digite o primeiro valor (A): "))
B = int(input("Digite o segundo valor (B): "))

if A > B:
    DIF = A - B
else:
    DIF = B - A

print(f"A diferença do maior pelo menor é: {DIF}")
