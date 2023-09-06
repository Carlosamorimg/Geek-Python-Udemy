
segundos = int(input("Digite um valor em segundos: "))


horas = segundos // 3600
segundos %= 3600
minutos = segundos  // 60
segundos %= 60

print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
