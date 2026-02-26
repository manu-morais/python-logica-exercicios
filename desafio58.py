cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break 
        print('Número inválido. Tente novamente. ')

    print(f'Você digitou o número {cont[numero]}')

    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()
        if resp in ('S', 'N'):
            break
        print('Resposta inválida. Digite S ou N.')

    if resp == 'N':
        print('Programa encerrado!')
        break
