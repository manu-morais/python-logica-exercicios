distancia = int(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    valor1 = distancia * 0.50
    print(f'O valor da viagem será R${valor1:.2f} ')
else:
    valor2 = distancia * 0.45
    print(f'O valor da viagem será R${valor2:.2f} ')
