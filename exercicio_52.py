
investidor1 = float(input("Informe o valor investido pelo primeiro apostador: "))
investidor2 = float(input("Informe o valor investido pelo segundo apostador: "))
investidor3 = float(input("Informe o valor investido pelo terceiro apostador: "))


valor_premio = float(input("Informe o valor total do prêmio: "))


total_investido = investidor1 + investidor2 + investidor3
proporcao_investidor1 = investidor1 / total_investido
proporcao_investidor2 = investidor2 / total_investido
proporcao_investidor3 = investidor3 / total_investido


premio_investidor1 = proporcao_investidor1 * valor_premio
premio_investidor2 = proporcao_investidor2 * valor_premio
premio_investidor3 = proporcao_investidor3 * valor_premio


print(f"O primeiro investidor receberá: R${premio_investidor1:,.2f}")
print(f"O segundo investidor receberá: R${premio_investidor2:,.2f}")
print(f"O terceiro investidor receberá: R${premio_investidor3:,.2f}")
