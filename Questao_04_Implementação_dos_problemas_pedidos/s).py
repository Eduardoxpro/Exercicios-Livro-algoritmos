
# s) Quatro operações básicas

print("s) Quatro operações")
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão: {a / b:.2f}" if b != 0 else "Divisão: impossível (divisor zero)")
print ("="*40)