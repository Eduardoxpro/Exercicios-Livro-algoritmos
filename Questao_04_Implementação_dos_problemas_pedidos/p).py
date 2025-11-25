
print ("p) Salario mensal: ")

Salariomensal = float(input("Digite o valor do seu salário mensal: "))
PercentualReajuste = float(input("Digite a porcentagem de reajuste salarial: "))
Novosalario = PercentualReajuste * Salariomensal / 100 + Salariomensal
print (f"O valor do salário atualizado é: {Novosalario:.2f}")