ano = int(input('Digite o ano desejado: '))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano} é um ano Bissexto!!!')
else:
    print(f'O ano de {ano} NÃO é um ano Bissexto!!!!!')
