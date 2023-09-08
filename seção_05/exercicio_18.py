
n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

operacao = int(input('Escolha a Operação:\n 1 = Soma \n 2 = Subtração \n 3 = Multiplicação \n 4 = Divisão \n: '))

match operacao:

    case 1 :
        print(f'O resultado de {n1} + {n2} é {n1 + n2}')
    case 2 :
        print(f'O resultado de {n1} - {n2} é {n1 - n2}')
    case 3 :
        print(f'O resultado de {n1} * {n2} é {n1 * n2}')
    case 4 :
        print(f'O resultado de {n1} / {n2} é {n1 / n2}')
    case '':
        print('Operação invalida')

       

