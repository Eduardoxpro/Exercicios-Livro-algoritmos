# Calculo bem em atraso 

print ("e) Calculo de bem em atraso: ")
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa da prestação: "))
tempo = float(input("Digite o tempo de atraso em meses:  "))
prestacao = valor + (valor * (taxa / 100) * tempo)
print (f"O valor total da prestação com juros é: {prestacao:.2f} R$ ")