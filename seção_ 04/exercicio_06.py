


cel = float(input('Digite a temperatura em Gruas Celsius: '))
f = (cel*9/5)+32
print(f'A conversão de {cel}º celsius em Fahrenheit é: {f}')

# 2º forma

temp_celcius = float(input('Informe uma temperatura em Celcius: '))
print('{} °C = {:.2f} °F'.format(temp_celcius, temp_celcius*(9/5)+32))