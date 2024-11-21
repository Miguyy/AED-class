print("\t\tMENU")
print("\t1- Inserir Países")
print("\t2- Consulta Países")
print("\t3- Consulta por continente")
print("\t4- Consulta nº Países")
print("\t5- Sair")

menu = input("\tOpção: ")

listaContinentes = ["Europa", "Ásia", "América", "África", "Oceania"]

def inserir_paises():
    pais = input("País: ")
    continente = input("Continente: ")
    
    if continente not in listaContinentes:
        print("Continente inválido. Tente novamente.")
        return
    
    with open("AED/RSF7/paises.txt", "a", encoding="utf-8") as t:
        linha = pais + ";" + continente
        t.write(linha + "\n")

def consulta_paises():
    print("\t\tPaíses\t\tContinente")
    print("-------------------------------------------------------------------")
    try:
        with open("AED/RSF7/paises.txt", "r", encoding="utf-8") as t:
            for linha in t:
                campos = linha.strip().split(";")
                print("\t\t", campos[0], "\t", campos[1])
    except FileNotFoundError:
        print("Ficheiro não encontrado.")

def consulta_continente():
    continente = input("Continente: ")
    print(f"\nPaíses no continente {continente}:")
    try:
        with open("AED/RSF7/paises.txt", "r", encoding="utf-8") as t:
            for linha in t:
                campos = linha.strip().split(";")
                if campos[1] == continente:
                    print("\t", campos[0])
    except FileNotFoundError:
        print("Ficheiro não encontrado.")

def consulta_numero_paises_continente():
    continente = input("Continente: ")
    paises = 0
    try:
        with open("AED/RSF7/paises.txt", "r", encoding="utf-8") as t:
            for linha in t:
                campos = linha.strip().split(";")
                if campos[1] == continente:
                    paises += 1
        print(f"Há {paises} países no continente : {continente}.")
    except FileNotFoundError:
        print("Ficheiro não encontrado.")

match menu:
    case '1':
        inserir_paises()
    case '2':
        consulta_paises()
    case '3':
        consulta_continente()
    case '4':
        consulta_numero_paises_continente()
    case '5':
        print("A sair.")
    case _:
        print("Opção inválida. Tenta novamente.")
    
