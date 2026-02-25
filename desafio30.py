produto = float(input('Qual o valor do produto? '))
print("""FORMAS DE PAGAMENTO
[1] À vista no dinheiro ou cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = produto - (produto * 10 / 100)
elif opcao == 2:
    total = produto - (produto * 5 / 100)
elif opcao == 3:
    total = produto
    parcela = total / 2
    print(f'Sua compra será parcelada 2x de R${parcela:.2f} sem juros')
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    totalparc= int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R$ {parcela:.2f} com juros')
else:
    total = 0
    print('Opção de pagamento inválida. Tente novamente!')
print(f'Sua compra de R${produto:.2f} vai custar R${total:.2f}')


