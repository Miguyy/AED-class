# Lista de cidades
cidades = ["Lisboa", "Porto", "Faro", "Coimbra", "Braga"]

# Solicitando ao utilizador as temperaturas para cada cidade
temperaturas = []
for cidade in cidades:
    while True:
        try:
            temp = float(input(f"Digite a temperatura de {cidade}: "))
            temperaturas.append(temp)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Calculando a média
media = sum(temperaturas) / len(temperaturas)

# Encontrando a cidade com a maior distância da média
distancia_max = 0
cidade_mais_longe = ""

for i in range(len(cidades)):
    distancia = abs(temperaturas[i] - media)
    if distancia > distancia_max:
        distancia_max = distancia
        cidade_mais_longe = cidades[i]

# Resultados
print(f"\nA média das temperaturas é: {media:.2f}°C")
print(f"A cidade mais longe da média é {cidade_mais_longe} com uma diferença de {distancia_max:.2f}°C")
