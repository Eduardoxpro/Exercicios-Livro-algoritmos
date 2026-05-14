#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos dolares ela pode comprar

DINHEIRO = int(input("Digite quanto você tem em carteira: "))
CARTEIRADOLAR = DINHEIRO // 3.27
print("Você pode comprar {} dolares" .format(CARTEIRADOLAR))
 