
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

delta = B ** 2 -4 * A * C
print(f"O valor de delta é: {delta} ")

if delta < 0:
    print ("não há solução real")

elif  delta > 0:
     print(" Há duas soluções reais e diferentes e diferentes")

else: 
     delta = 0 
     print ("há apenas uma soluçao real")
    
