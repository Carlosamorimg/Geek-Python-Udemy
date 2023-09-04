

kel = float(input("Digite a temperatura em Graus Kelvin: "))
cel = kel -273.15
print(f'A conversão de {kel}º Kelvin em Graus Celsius é: {cel}')

# 2º forma

temp_kelvin = float(input('Informe uma temperatura em Kelvin: '))
print('{} °K = {:.2f} °C'.format(temp_kelvin, temp_kelvin - 273.15))