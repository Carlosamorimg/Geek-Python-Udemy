dia = int(input('Digite um numero entre 1 e 7, para verificar que dia da semana é: '))

match dia:

    case 1:
        print ("domingo")
    case 2:
        print ("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print('Quarta-Feira')
    case 5:
        print('Quinta-Feira')
    case 6:
        print('Sexta-Feira')
    case 7:
        print('Sabado')
    case _:
        print('Numero invalido')
