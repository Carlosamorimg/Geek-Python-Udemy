sexo = input('Digite seu Sexo: ')
altura = float(input('Digite seu Altura: '))

if sexo == 'masculino':
    print(f'Seu peso ideal é {(72.7 * altura)- 58:.2f}')
else:
    print(f'Seu peso ideal é {(62.1*altura)-44.7:.2f}')

