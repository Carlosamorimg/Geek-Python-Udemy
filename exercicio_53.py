
comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))
largura_terreno = float(input("Digite a largura do terreno em metros: "))


preco_tela_por_metro = float(input("Digite o preço do metro de tela em reais: "))


area_terreno = comprimento_terreno * largura_terreno


custo_total = area_terreno * preco_tela_por_metro


print(f"O custo total para cercar o terreno com tela é de R${custo_total:.2f}")
