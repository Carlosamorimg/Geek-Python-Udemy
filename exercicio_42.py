sal_base= float(input('Digite o Valor do Salario Base: R$ '))

grat = sal_base * 0.05
impos = sal_base * 0.07

print(f'Salario a Receber: R$ {sal_base - impos + grat}')


