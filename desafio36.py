soma = 0
for c in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os números pares é {soma}')
