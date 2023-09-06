
a = int(input('Digite um numero inteiro '))
b = int(input('Digite outro numero inteiro '))
c = int(input('Digite outro numero inteiro '))
soma = a + b + c

print(f"A soma dos tres valores é {soma}")


# 2º forma
a, b, c = map(int, list(input('Informe três valores inteiros: ').split()))
print(f'A soma de {a} + {b} + {c} é {a+b+c}')
