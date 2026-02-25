somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if maioridadehomem == 0 or idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
if nomevelho != '':
    print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
else:
    print('Não houve homens cadastrados.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
