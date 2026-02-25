import random

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome de terceiro aluno: ')
al4 = input('Digite o número do quarto aluno: ')
alunos = [al1, al2, al3, al4]
sorteado = random.choice(alunos)
print(f'O aluno sorteado foi {sorteado}')
