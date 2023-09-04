
from math import sqrt

a = float(input('Entre com o 1º valor: '))
b = float(input('Entre com o 2º valor: '))

cat_a = a ** 2
cat_b = b ** 2

#print (f'{cat_a} {cat_b}')
h = sqrt(cat_a + cat_b)

print(f'A hipotenusa do triangulo, cujos os lados são {a} e {b} é {h:.2f}')


# 2º forma 

a, b = map(float, input('Informe os dois catetos: ').split())
print('Hipotenusa: {}'.format((a**2 + b**2)**0.5))