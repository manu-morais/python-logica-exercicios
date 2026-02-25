from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maior... Tente novamente.')
        if jogador > computador:
            print('Menor... Tente novamente.')
print(f'Parabéns! Você acertou com {palpite} tentativas.')