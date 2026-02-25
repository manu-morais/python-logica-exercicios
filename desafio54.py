from random import randint
v = 0
print('=-'*25)
print('VAMOS JOGAR PAR OU IMPAR!')
print('=-'*25)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*50)
    print(f'Você jogou {jogador} e o computador jogou {computador}. A soma é {total}!')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-'*50)
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            print('=-' * 25)
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            print('=-' * 25)
            break
print(f'GAME OVER! Você venceu {v} vezes.')


