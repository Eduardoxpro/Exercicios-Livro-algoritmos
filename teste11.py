#Faça um programa que leia a largura ea altura de uma parede, em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-la, 
# sabendo que cada litro de tinta pinta uma área de 2m quadrados

LARGURA = int(input("Digite a largura da parede em metros: "))
ALTURA = int(input("Digite a altura da parede em metros: "))
AREA = LARGURA * ALTURA
LITROTINTA = AREA // 2
print ("A quantidade de litros de tinta necessária para pintar essa parede é {}" .format(LITROTINTA))