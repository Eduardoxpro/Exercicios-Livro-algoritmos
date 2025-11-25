
# x) Raiz de qualquer índice

print("x) Raiz de qualquer índice")
numero = float(input("Número: "))
indice = float(input("Índice da raiz: "))

if numero < 0 and indice % 2 == 0:
    print("Não existe raiz real de número negativo com índice par.")
else:
    resultado = numero ** (1/indice)
    print(f"Raiz {indice}ª de {numero} = {resultado:.4f}")