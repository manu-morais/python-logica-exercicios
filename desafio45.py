n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS 
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}!')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação ente {n1} e {n2} é {multiplicar}!')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}!')
    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!Tente novamente!')
print('Fim do programa!')



