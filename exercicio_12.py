

mi= float(input('Digite a distancia me milhas: '))
k = 1.61 * mi
print(f'A conversão de {mi} milhas em Kilometro é {k}')

# 2º forma 

distancia_milhas = float(input('Informe uma distância em milhas: '))
print('{} milhas = {:.2f} quilômetros'.format(distancia_milhas, distancia_milhas*1.61))