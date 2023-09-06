v_h = float(input('Qual o Valor da Hora Trabalhada: R$ '))

h_t = float(input('Digite o total de Horas Trabalhadas:  '))

valor= v_h * h_t
print(f'O valor a ser recebido será de R$ {valor + valor * 0.10: .2f}, co um acrescimo de 10 %')

