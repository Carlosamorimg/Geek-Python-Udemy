# leia a temperatura em Fahrenheit e apresente em Celsius.
# formula C= 5*(f-32)/9



fa = float(input("Digite a Temperatura em Fahrenheit: "))
cel = 5*(fa -32)/9
print(f'A conversão de {fa}º fahrenheit em Celsius é {cel}º celsius')