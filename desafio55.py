tot18 = toth = totm20 = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'{' FIM DO PROGRAMA ':=^30}')
print(f'Total de pessoas com mais de 18 anos cadastradas: {tot18}')
print(f'Total de homens cadastrados: {toth}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {totm20}')






