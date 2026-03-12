pessoas = list()
dados = list ()
pesomaior = pesomenor = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if len(dados) == 0:
        pesomaior = pesomenor = pessoas[1]
    else:
        if pessoas[1] > pesomaior:
            pesomaior = pessoas[1]
        if pessoas[1] < pesomenor:
            pesomenor = pessoas[1]

    dados.append(pessoas[:])
    pessoas.clear()
    
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    if pergunta in 'N':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(dados)} pessoas!')
print(f'O maior peso foi de {pesomaior}kg. Peso de ', end='')
for p in dados:
    if p[1] == pesomaior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {pesomenor}kg. Peso de ', end='')
for p in dados:
    if p[1] == pesomenor:
        print(f'[{p[0]}] ', end='')