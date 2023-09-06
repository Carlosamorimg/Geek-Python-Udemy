valor_pro = float(input('Qual o Valor do Produto: R$ '))
v_d = valor_pro -valor_pro * 0.10

print(f'Total a pagar com 10 % de Desconto: R$ {v_d}')
print (f'Valor parcelado em 3x sem juros, três parcelas de R$ {valor_pro/3:.2f}')
print(f'Comissão vendedor pagamento a Vista R$ {v_d * 0.05}')
print(f'Comissão vendedor pagamento parcelado R$ {valor_pro * 0.05}')


