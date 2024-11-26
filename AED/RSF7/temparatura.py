import os

caminho_arquivo = os.path.join("files", "temperatura.txt")

def consulta_data():
    data_pedida = input("Data da Consulta (formato: AAAA-MM-DD): ").strip()
    print("\n\t\tData\t\tHora\t\tTemperatura")

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    encontrou = False  

    for linha in linhas:
        campos = linha.strip().split(";")  
        data = campos[0]  
        hora = campos[1]
        temperatura = campos[2]

        if data == data_pedida:
            encontrou = True
            print(f"\t\t{data}\t{hora}\t\t{temperatura}°C")
    
    if not encontrou:
        print("\nNão foram encontrados registos para a data fornecida.")

def consulta_stats():
    listaTemperaturas=[]
    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()
    for linha in linhas:
        campos = linha.strip().split(";")
        temperatura = float(campos[2])  
        listaTemperaturas.append(temperatura)

    if listaTemperaturas:
        temperatura_min=min(listaTemperaturas)
        temperatura_max=max(listaTemperaturas)
        temperatura_media=sum(listaTemperaturas)/len(listaTemperaturas)
    print(f"O maior valor da temperatura foi de {temperatura_min}")
    print(f"O menor valor da temperatura foi de {temperatura_max}")
    print(f"A média foi de {temperatura_media:.2f}")

def menu_function():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Consulta por data")
        print("\t 2- Consulta Estatística")
        print("\t 0- Sair")

        menu=input("Opção: ")

        match menu:
            case '1':
                consulta_data()
            case '2':
                consulta_stats()
            case '0':
                print("A sair do programa.")
                break
            case _:
                print("Informação incorrecta. Insira novamente os detalhes.")
                continue
menu_function()
