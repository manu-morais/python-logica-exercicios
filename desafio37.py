pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = pt + (10 - 1) * razao
for c in range(pt,decimo + razao,razao):
   print(c, end=' -> ')
print('FIM')

