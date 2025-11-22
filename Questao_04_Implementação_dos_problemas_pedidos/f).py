# f) Troca de valores entre variáveis A e B
print("f) TROCA DE VALORES")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
print(f"Antes → A = {A}, B = {B}")
temp = A    # variável temporária
A = B
B = temp
print(f"Depois → A = {A}, B = {B}")
print("="*40)