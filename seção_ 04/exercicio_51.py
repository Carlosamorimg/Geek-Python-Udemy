import math


x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))


distancia_origem = math.sqrt(x ** 2 + y ** 2)


print(f"A distância até a origem (0, 0) é: {distancia_origem:.2f}")

