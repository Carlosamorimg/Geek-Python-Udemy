a, b = map(float,list(input('Digite as duas notas: ').split()))

if a > 0 and b > 0 and a < 10 and b < 10:
    print(f'A media entre {a} e {b} é {(a+b)/2}')
else:
    print('Notas ausentes ou invalidas !!!!!')

