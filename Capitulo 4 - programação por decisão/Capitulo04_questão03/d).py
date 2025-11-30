
print("=== CÁLCULO DE MÉDIA ESCOLAR COM EXAME ===\n")

n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))


md1 = (n1 + n2 + n3 + n4) / 4

print()  

if md1 >= 7:
    print("Aprovado")
    print(f"MD = {md1:.1f}")
else:
    
    ne = float(input("\nDigite a nota do exame: "))
    
    md2 = (md1 + ne) / 2
    
    if md2 >= 5:
        print("Aprovado em exame")
    else:
        print("Reprovado")
    
    print(f"MD = {md2:.1f}")
