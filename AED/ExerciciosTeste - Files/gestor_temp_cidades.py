import os   

sub_pasta = "files"
caminho_arquivo = os.path.join(sub_pasta, "temp_cidades.txt")

cidades = ["Porto", "Maia", "Matosinhos", "Vila do Conde", "Póvoa de Varzim", "Gondomar", "Gaia"]
temperaturas = []

def adicionar_temp():
    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'temp_cidades.txt' não existe. Vai ser criado.")
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.close()

    for cidade in cidades:
        while True:
            try:
                temp = float(input(f"Escreva a temperatura de {cidade} entre 1-40: "))  
                if 1 <= temp <= 40:  
                    temperaturas.append((cidade, temp))  
                    break  
                else:
                    print("Entrada inválida. Por favor, escreve um número entre 1 e 40.") 
            except ValueError:  
                print("Entrada inválida. Por favor, escreve um número.") 

    t = open(caminho_arquivo, "a", encoding="utf-8")
    for cidade, temp in temperaturas:
        t.write(f"{cidade};{temp}\n")
    t.close()
    
    print("As temperaturas foram adicionadas com sucesso!")

def calc_media_e_cidades():
    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines() 
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";") 
        cidade = campos[0]
        temperatura = float(campos[1])
        temperaturas.append(temperatura)

    media = sum(temperaturas) / len(temperaturas)  
    distancia_max = 0  
    cidade_mais_longe = " "  
    
    for i in range(len(cidades)):
        distancia = abs(temperaturas[i] - media)
        if distancia > distancia_max: 
            distancia_max = distancia 
            cidade_mais_longe = cidades[i] 

    print(f"\nA média das temperaturas é: {media:.2f}ºC")
    print(f"A cidade mais longe da média é {cidade_mais_longe} com uma diferença de {distancia_max:.2f}ºC")

def menu_function():
    while True:
        print("\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t MENU")
        print("\t 1- Adicionar Temperaturas")
        print("\t 2- Calcular Média e Identificar Cidades")
        print("\t 0- Sair")

        menu=input("Opção: ")

        match menu:
            case '1':
                adicionar_temp()
            case '2':
                calc_media_e_cidades()
            case '0':
                print("A sair.")
                break
            case _:
                print("Foi impossível de compreender. Tente novamente.")
                continue
menu_function()

