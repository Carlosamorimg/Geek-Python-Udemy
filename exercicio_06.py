# leia a temperatura em Gruas Celsius e apresente-a convertida em gruas fahrenheit.
# fomula F= C*(9.0/5.0)+ 32.0


cel = float(input('Digite a temperatura em Gruas Celsius: '))
f = (cel*9/5)+32
print(f'A conversão de {cel}º celsius em Fahrenheit é: {f}')