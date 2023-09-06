
altura_degrau_cm = float(input("Digite a altura do degrau em centímetros: "))
altura_desejada_metros = float(input("Digite a altura desejada em metros: "))

# Converte a altura desejada para centímetros
altura_desejada_cm = altura_desejada_metros * 100

# Calcula a quantidade de degraus necessários
quantidade_degraus = altura_desejada_cm / altura_degrau_cm

print(f"Você precisará subir {quantidade_degraus:.2f} degraus para alcançar a altura desejada.")
