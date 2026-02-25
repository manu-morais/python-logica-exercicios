soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
     soma += c
print(f'A soma de todos os valores ímpares divisíveis por 3 de 1 até 500 é {soma}')
