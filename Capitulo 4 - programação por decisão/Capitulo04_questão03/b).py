# Lê o número (pode ser positivo ou negativo)
N = int(input("Digite um número (pode ser negativo): "))

# Se for negativo, multiplica por -1
if N < 0:
    N = N * (-1)

# Mostra o número sempre positivo
print("O valor positivo é:", N)
