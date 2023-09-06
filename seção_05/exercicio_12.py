import math

a = int(input('Digite um numero: '))

if a <= 0:
    print('Numero invalido')
else:
    print(f'O calculo do logaritmo de {a} é {math.log(a)}')

