n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro Numero: '))

opcao = int(input('Escolha a Opção: \n1- soma de 2 numeros: \n2- Diferença entre dois numeros: (Maior pelo Menor) \n3- Produto entre dois numeros: \n4- Divisão entre dois numeros: ( o denominador não pode ser zero.)\n'))

match opcao:
    case 1:
        print(f'A soma de {n1} + {n2} é: {n1 + n2}')
    case 2:
        if n1 > n2:
            print(f'A diferença entre {n1} e {n2} é {n1 - n2}')
        else:
            print(f'A diferença entre {n2} e {n1} é {n2-n1}')
    case 3:
        print(f'O produto entre {n1} e {n2} é {n1*n2}')
    case 4:
        if n2 != 0:
            print(f'A divisão de {n1} por {n2} é {n1/n2}'
        )
        else:
            print(f'Não é possivel dividir {n1} por {n2}')
