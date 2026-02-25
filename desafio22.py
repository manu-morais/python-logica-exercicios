idade = int(input('Qual a sua idade? '))
if idade < 18:
    minimo = 18 - idade
    print(f'Ainda vai se alistar no exército e falta {minimo} anos para o prazo!')
elif idade == 18:
    print('Está no prazo para se alistar no exército!')
else:
   maximo = idade - 18
   print(f'Passou {maximo} anos do prazo para se alistar no exército!')
