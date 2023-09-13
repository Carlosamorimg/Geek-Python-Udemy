a, b, c = map(float, list(input('Digite tres medidas para verificar se é um triangulo: ').split()))

if a < (b + c):
    if a == b and b == c and c == a:
        print('Isso é um Triangulo Equilatero!!!')
    elif a == b or b == c or c == a:
        print('Isso é un Triangulo Isosceles!!!!')
    elif a != b and b != c and c != a:
        print('Isso é um Triangulo Escaleno!!!')
