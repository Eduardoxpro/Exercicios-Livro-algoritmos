# 4.b) Ler temperatura em Fahrenheit e mostrar em Celsius
f = float(input("Digite a temperatura em graus Fahrenheit: "))
c = (f - 32) * 5/9
print(f"b) {f}°F equivale a {c:.2f}°C")
print("="*40)