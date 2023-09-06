import math

num = float(input('Digite um numero: '))

if num > 0:
    print(f'A Raiz quadrada de {num} é {math.sqrt(num)}')
    print(f'O quadrado de {num} é {pow(num, 2)}')

