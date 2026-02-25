print('GERADOR DE PA')
print('-=' * 32)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo} -> ' , end='')
    termo += razao
    cont += 1
print('FIM')
print('-=' * 32)