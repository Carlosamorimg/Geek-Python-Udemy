numero = int(input("Digite um número inteiro maior que 0: "))

if numero <= 0:
    print("Número inválido. O número deve ser maior que 0.")
else:
    soma = 0
    for i in range(1, numero + 1):
        soma += i

    print(f"A soma dos números de 1 até {numero} é: {soma}")
