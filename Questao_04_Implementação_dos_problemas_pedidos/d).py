# 4.d) Calcular quantos litros de combustível são gastos na viagem
tempo = float(input("Digite o tempo da viagem (em horas): "))
velocidade = float(input("Digite a velocidade média (em km/h): "))
distancia = tempo * velocidade
litros = distancia / 12
print(f"d) A Distância percorrida é: {distancia:.2f} km")
print(f" O Combustível gasto é: {litros:.2f} litros")
print(f" A velocidade média é: {velocidade:.2f} km/h")
print(f" O tempo gasto na viagem é: {tempo:.2f} horas")