# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabahos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random 

def sortear_alunos(aluno01, aluno02, aluno03, aluno04):
      alunos = [aluno01, aluno02, aluno03, aluno04]
      return random.choice(alunos)

aluno01 = str(input("Digite o nome dos aluno01:" ))
aluno02 = str(input("Digite o nome dos aluno02:" ))
aluno03 = str(input("Digite o nome dos aluno03:" ))
aluno04 = str(input("Digite o nome dos aluno04:" ))

escolhido = sortear_alunos(aluno01, aluno02, aluno03, aluno04)
print("O aluno escolhido foi: {}" .format(escolhido))
