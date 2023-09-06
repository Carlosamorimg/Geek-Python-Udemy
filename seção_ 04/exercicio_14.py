


pi = 3.14159265358979323846

grau= float(input('Digite o Grau do angulo em questão: '))
rad = grau*pi/180
print(f'Radiano = {rad}')

# 2º forma 

from math import radians
angulo_graus = float(input('Informe um ângulo em graus: '))
print('{}° = {:.3f} radianos'.format(angulo_graus, radians(angulo_graus)))