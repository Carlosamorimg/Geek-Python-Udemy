# a importancia de R$ 78.000,00 será dividida entre tres ganhadores
# 1º receberá 46%
# 2º receberá 32%
# 3º receberá o restante



a = 780000.00 *0.46
b = 780000.00 *0.32
c = 780000.00 - (a+b)


print(f'O 1º receberá R$ {a:,.2f}')
print(f'O 2º receberá R$ {b:,.2f}')
print(f'O 3º receberá R$ {c:,.2f}')


total = a+b+c
print(f'Total R$ {total:,.2f}')
