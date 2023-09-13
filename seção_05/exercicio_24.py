valor = float(input("Digite o Valor da Compra R$: "))
estado = input("Digite o Estado onde Será feita a Compra: ")


if estado == 'Minas Gerais':
    print(f'O valor final com os Impostos é de R$: {valor + valor * 0.07:.2f}')
elif estado == 'São Paulo':
    print(f'O valor final com os Impostos é de R$: {valor + valor * 0.12:.2f}')
elif estado == 'Rio de Janeiro':
    print(f'O valor final com os Impostos é de R$: {valor + valor * 0.15:.2f}')
elif estado == 'Mato Grosso do Sul':
    print(f'O valor final com os Impostos é de R$: {valor + valor * 0.08:.2f}')
else:
    print(f'Lamento, Não atendemos a região do {estado}')


