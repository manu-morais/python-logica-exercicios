nome = input('Digite seu nome completo: ').strip()

print(f'O seu nome com todas as letras maiúsculas fica: {nome.upper()}')
print(f'O seu nome com todas as letras minúculas fica: {nome.lower()}')
print(f'O seu nome tem {len(nome) - nome.count(' ')} letras')
print(f'O seu primeiro nome tem {nome.find(' ')} letras')

