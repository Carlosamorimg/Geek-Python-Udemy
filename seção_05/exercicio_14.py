t_l = float(input('Digite a nota do Trabalho de Laboratorio: '))
a_s = float(input('Digite a nota da Avaliação Semestral: '))
e_f = float(input('Digite a Nota do Exame Final: ')) 

media = ((t_l * 2)+ (a_s * 3) + (e_f * 5))/ 10

if media >= 0 and media <= 2.9:
    print('Aluno Reprovado!!!!')
elif media >= 3 and media <= 4.9:
    print('Aluno de Recuperação!!')
else:
    print('Aluno Aprovado!!!!')


