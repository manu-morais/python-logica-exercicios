sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo [F/M]: ')).strip().upper()
print(f'Sexo {sexo} cadastrado com sucesso!')