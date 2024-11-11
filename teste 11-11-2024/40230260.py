cidades = ["Porto", "Maia", "Matosinhos", "Vila do Conde", "Póvoa de Varzim", "Gondomar", "Gaia"]  # lista das cidades
temperaturas = []  # lista para guardar as temperaturas

def dadosEstatistica(temperaturas):  # criação da função
    for cidade in cidades:  # para cidades em cidades, então...
        while True:  # enquanto verdade, então
            try:  # vai tentar
                temp = float(input(f"Escreva a temperatura de {cidade} entre 1-40: "))  # utilizador selecciona a temperatura
                if 1 <= temp <= 40:  # validação para garantir que a temperatura está no intervalo
                    temperaturas.append(temp)  # a lista vai pegar nas temperaturas inseridas e guardar
                    break  # STOP
                else:
                    print("Entrada inválida. Por favor, escreve um número entre 1 e 40.")  # se estiver fora do intervalo
            except ValueError:  # captura erros de entrada não numérica
                print("Entrada inválida. Por favor, escreve um número.")  # pede para colocar novamente

    # criação da média
    media = sum(temperaturas) / len(temperaturas)  # soma as temperaturas e divide pelo número de elementos
    distancia_max = 0  # criação da variável da distância máxima
    cidade_mais_longe = ""  # criação da variável da cidade mais longe

    for i in range(len(cidades)):
        distancia = abs(temperaturas[i] - media)  # cálculo do valor absoluto da diferença em relação à média
        if distancia > distancia_max:  # se a distância for maior que a distância máxima encontrada
            distancia_max = distancia  # atualiza a distância máxima
            cidade_mais_longe = cidades[i]  # atualiza a cidade mais longe

    # resultados
    print(f"\nA média das temperaturas é: {media:.2f}ºC")
    print(f"A cidade mais longe da média é {cidade_mais_longe} com uma diferença de {distancia_max:.2f}ºC")

# chama a função para executar
dadosEstatistica(temperaturas)
