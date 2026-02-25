print('GERADOR DE PA')
print('-=' * 33)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ' , end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos temmos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados!')


