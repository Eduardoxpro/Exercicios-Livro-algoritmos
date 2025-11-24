# l) Conversor Real → Dólar
print("l) CONVERSOR REAL → DÓLAR")
cotacao = float(input("Cotação do dólar hoje (R$): "))
reais = float(input("Quantos reais você tem? "))
dolares = reais / cotacao
print(f"Você pode comprar US$ {dolares:.2f}")
print("="*40)


print (" Conversor de Real em dolar")
cotacao = float(input("Digite o valor da cotação do dolar hoje "))
reais = float(input(" Quantos reais deseja converter? "))
dolares = reais /  cotacao
print(f"Você tem {dolares:.2f} $ ")
print("-"*40)