# Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a paga, sabendo
# que o carro custa R$ 60 por dia e R$ 0,15 Por Km rodado

KMPERCORRIDOS = float(input("Digite a quantidade de KM percorridos: "))
DIASALUGADOS = int(input("Digite a quantidade de dias alugados: "))
PRECOTOTAL = KMPERCORRIDOS * 0.15 + DIASALUGADOS * 60
print ("O preço total dos dias alugados e km percorridos é: {:.2f}" .format(PRECOTOTAL)) 