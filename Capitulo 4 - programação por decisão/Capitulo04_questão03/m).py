nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")

if sexo == "M" or sexo == "F":
    if sexo == "M":
        print(f"Ilmo. Sr. {nome}")
    else:
        print(f"Ilma. Sra. {nome}")
else:
    print("Sexo informado inválido")
