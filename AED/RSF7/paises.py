import os

listaContinente=["Europa", "Ásia", "África", "América", "Oceania"]
sub_pasta = "files"
caminho_arquivo = os.path.join(sub_pasta, "paises1.txt")

def inserir_paises():
    pais = input("Indique o país: ").strip()
    continente = input("Indique o continente: ").strip()

    if continente not in listaContinente:
        print("Continente inválido. Tente novamente.")
        return

    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'paises1.txt' não existe. Vai ser criado.")
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.close()

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        if linha.strip().split(";")[0].lower() == pais.lower():
            print(f"O país '{pais}' já existe no ficheiro.")
            return
        
    t = open(caminho_arquivo, "a", encoding="utf-8")
    linha = pais + ";" + continente
    t.write(linha + "\n")
    t.close()

    print(f"O país '{pais}' foi adicionado com sucesso.")

def consulta_paises():
    print("\t\t País \t\t Continente")
    print("------------------------------------------------------------------")

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines() 
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";") 
        print(f"\t\t {campos[0]} \t\t {campos[1]}") 

def consulta_por_continente():
    continente = input("Indique o continente: ")
    print("\t\t País \t\t Continente")
    print("------------------------------------------------------------------")

    encontrar_Pais = False  

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  
        if campos[1] == continente:  
            print(f"\t\t {campos[0]} \t\t {continente}") 
            encontrar_Pais = True  
    if not encontrar_Pais:
        print("Ainda não existem países para esse continente.")

def consulta_num_paises():
    
    contador_europa = 0
    contador_asia = 0
    contador_america = 0
    contador_africa = 0
    contador_oceania = 0

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  
        
        pais = campos[0] 
        continente = campos[1] 
        
        if continente == "Europa":
            contador_europa += 1
        elif continente == "Ásia":
            contador_asia += 1
        elif continente == "América":
            contador_america += 1
        elif continente == "África":
            contador_africa += 1
        elif continente == "Oceania":
            contador_oceania += 1

    print("--------------------------------------------")
    print("\nNúmero total de países por continente:")
    print("\n")
    print(f"Europa - {contador_europa}")
    print(f"Ásia - {contador_asia}")
    print(f"América - {contador_america}")
    print(f"África - {contador_africa}")
    print(f"Oceania - {contador_oceania}")


def menu_function():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Inserir Países")
        print("\t 2- Consulta países")
        print("\t 3- Consulta por continente")
        print("\t 4- Consulta nº países")
        print("\t 0- Sair")

        menu=input("Opção: ")

        match menu:
            case '1':
                inserir_paises()
            case '2':
                consulta_paises()
            case '3':
                consulta_por_continente()
            case '4':
                consulta_num_paises()
            case '0':
                print("A sair do programa")
                break
            case _:
                print("Informação incorrecta. Insira novamente os detalhes.")
                continue
menu_function()
