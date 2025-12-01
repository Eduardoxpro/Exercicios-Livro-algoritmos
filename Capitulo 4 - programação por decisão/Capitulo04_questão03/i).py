# i) Faça um programa que receba do usuário um número N e uma frase.
# Depois imprima a frase N vezes.

N = int(input("Digite o número de repetições: "))
frase = input("Digite a frase: ")

for _ in range(N):
    print(frase)

# ou mais simples:
print(frase * N)  # repete a string N vezes (só funciona se não precisar de quebras de linha extras)
