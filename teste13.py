#Faça um programa que leia o salário de um funcionário e mostre
#seu novo salário com 15% de aumento

SALARIO = int(input("Digite o seu salário: "))
NS = SALARIO * 1.15
print("Seu salário atualizado é: {:.2f} " .format(NS))