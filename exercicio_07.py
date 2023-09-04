

fa = float(input("Digite a Temperatura em Fahrenheit: "))
cel = 5*(fa -32)/9
print(f'A conversão de {fa}º fahrenheit em Celsius é {cel}º celsius')


# 2º forma


temp_fahrenheit = float(input('Informe uma temperatura em Fahrenheit: '))
print('{} °F = {:.2f} °C'.format(temp_fahrenheit, 5*(temp_fahrenheit - 32)/9))