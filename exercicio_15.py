


pi = 3.14159

rad= float(input('Digite o valor do angulo em Radiano: '))
g = rad *180/pi
print(f'Graus = {g}')

# 2º forma 

from math import degrees
angulo_radianos = float(input('Informe um ângulo em radianos: '))
print('{} radianos = {:.3f}°'.format(angulo_radianos, degrees(angulo_radianos)))