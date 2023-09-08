n1, n2 , n3 = map(float, list(input('Digite as tres notas: ').split()))

p1, p2, p3 = map(int, list(input('Digita o peso de cada nota: ').split()))
media = (n1+ n2+ n3 * 2)/4
#m_p = ((n1*p1) + (n2*p2) + (n3 * p3))/ (p1 + p2 + p3)
#print(f'{m_p:.2f}')



if media >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')
