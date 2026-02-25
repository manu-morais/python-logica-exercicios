casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print(f'\nPara pagar uma casa de R$ {casa:.2f} em {anos} anos,', end=' ')
print(f'a pretação será de R$ {prestacao:.2f})')
if prestacao <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')
