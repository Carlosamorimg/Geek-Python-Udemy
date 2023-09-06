# Recebe a letra maiúscula do usuário
letra_maiuscula = input("Digite uma letra maiúscula: ")

# Converte a letra maiúscula em minúscula usando a tabela ASCII
valor_ascii = ord(letra_maiuscula)
if 65 <= valor_ascii <= 90:
    letra_minuscula = chr(valor_ascii + 32)
    print(f"A letra minúscula correspondente é: {letra_minuscula}")
else:
    print("Você não digitou uma letra maiúscula válida.")



# 2º forma

# Recebe a letra maiúscula do usuário
letra_maiuscula = input("Digite uma letra maiúscula: ")

# Converte a letra maiúscula em minúscula usando a tabela ASCII
valor_ascii = ord(letra_maiuscula)
valor_ascii += 32 * (valor_ascii >= 65 and valor_ascii <= 90)

# Exibe a letra minúscula correspondente
letra_minuscula = chr(valor_ascii)
print(f"A letra minúscula correspondente é: {letra_minuscula}")
