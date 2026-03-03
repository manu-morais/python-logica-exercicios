numeros = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r in 'N':
        break

print(f'Lista completa: {numeros}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')