print("=== ORDEM CRESCENTE DE 3 NÚMEROS ===\n")

# Leitura dos três valores
a = int(input("Digite o 1º valor (A): "))
b = int(input("Digite o 2º valor (B): "))
c = int(input("Digite o 3º valor (C): "))

print("\nValores originais:", a, b, c)

# Vamos ordenar usando apenas comparações e trocas
# Ideia: comparar aos pares e trocar se estiverem fora de ordem

if a > b:           # se A maior que B → troca
    a, b = b, a     # troca A com B

if b > c:           # se B maior que C → troca
    b, c = c, b     # troca B com C

if a > b:           # após a troca anterior, pode ser que A e B ainda estejam errados
    a, b = b, a     # troca A com B novamente (garante que A <= B <= C)

# Agora a, b e c estão em ordem crescente
print("Valores em ordem crescente:", a, b, c)