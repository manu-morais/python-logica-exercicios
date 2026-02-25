salario = float(input('Digite o seu salário em R$: '))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print(f'Quem ganhava {salario:.2f} passa a ganhar {novo:.2f}')
