velocidade = int(input('Seu carro está a quantos km? '))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print('Você foi multado!')
    print(f'A sua multa foi de R$ {multa:.2f}')
else:
    print('Você está dentro do limite de velocidade permitido!')
