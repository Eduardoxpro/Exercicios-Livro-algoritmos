# t) Velocidade média de um pojetil (m/s)

velocidade = int(input("Digite a velocidade: "))
tempo = int(input("Digite o tempo em minutos: "))
distancia = int(input("digite a distância em quilômetros: "))
projetilms = distancia * 1000 / tempo * 60
print (f"A velocidade média de um projeto é: {projetilms:.2f}")
print ("="*40)