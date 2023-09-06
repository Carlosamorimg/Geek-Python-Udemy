


cel = float(input('Digite a temperatura em Graus Celsius: '))
kel = cel + 273.15
print(f'A conversão de {cel}ª Celsius em Graus Kelvin é: {kel}')

# 2º forma

temp_celcius = float(input('Informe uma temperatura em Celcius: '))
print('{} °C = {:.2f} °K'.format(temp_celcius, temp_celcius + 273.15))