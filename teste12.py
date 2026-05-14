#Faça um algoritmo que leia o preço de um produto
# E mostre seu novo preço com 5% de desconto

PRODUTO = int(input("Digite o preço do produto que deseja: "))
DESCONTO = (5 / 100) * PRODUTO
NP = PRODUTO - DESCONTO
print ("O novo preço com desconto aplicado é: {} " .format(NP))