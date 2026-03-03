numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))

    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print('-= ' * 30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontarado na lista!')
