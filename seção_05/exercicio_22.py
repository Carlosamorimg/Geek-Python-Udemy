idade, tem_ser = map(int, list(input('Digite sua idade e seu Tempo total de serviço: ').split()))

if idade >= 65:
    print('Você pode se Aposentar por idade!!!')
elif tem_ser >= 30:
    if idade - tem_ser >= 16:
        print('Você pode se aposentar por Tempo de Serviço!!!!')
    else:
        print('Á um inconsistencia nos dados!!!')
elif idade >= 60 and tem_ser >= 25:
    print('Você pode se aposentar pela combinação de Idade mais Tempo de Serviço!!!')
else:
    print('Você não tem nenhum dos requisitos para se aposentar!!')
