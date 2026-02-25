nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Você está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('Você está em RECUPEREÇÃO!')
else:
    print('Você está APROVADO!')