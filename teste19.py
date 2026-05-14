# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random 

def sortear_alunos(aluno01, aluno02, aluno03, aluno04):
      alunos = [aluno01, aluno02, aluno03, aluno04]
      return random.choice(alunos)

escolhido = sortear_alunos("Maria", "Ana", "Pedro", "João")
print("O aluno escolhido foi: {}" .format(escolhido))