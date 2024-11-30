import os   

sub_pasta="files"
caminho_arquivo=os.path.join(sub_pasta, "livros.txt")

listaGenero=["Romance", "Ficção", "Fantasia", "Terror", "Poesia"]

def adicionar_livro():

    titulo_livro=input("Indique o título do livro: ")
    autor_livro=input("Indique o autor do livro: ")
    genero_livro=input("Indique o género do livro: ")

    if genero_livro not in listaGenero:
        print("Género inválido. Tente novamente.")
        return

    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'livros.txt' não existe. Vai ser criado.")
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.close()

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        if linha.strip().split(";")[0].lower() == titulo_livro.lower():
            print(f"O livro '{titulo_livro}' já existe no ficheiro.")
            return
        
    t = open(caminho_arquivo, "a", encoding="utf-8")
    linha = titulo_livro + ";" + autor_livro + ";" + genero_livro
    t.write(linha + "\n")
    t.close()

    print(f"O livro '{titulo_livro}' foi adicionado com sucesso.")

def registar_livros():
    print("\t\t\t Título \t\t\t Autor \t\t\t Género")
    print("---------------------------------------------------------------------------------------------------------------")

    encontrar = False
    
    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines() 
    t.close()
    
    for linha in linhas:
        campos = linha.strip().split(";") 
        if len(campos)==3:
            print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]}")
            encontrar=True
    if not encontrar:
        print("\n\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("Nenhum livro foi encontrado.")

        
def consultar_livro_genero():
    genero_livro = input("Indique o género do livro: ")

    encontrar = False  

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  

        if campos[2] == genero_livro:  
            if not encontrar:  
                print("\t\t\t Título \t\t\t Autor \t\t\t Género")
                print("---------------------------------------------------------------------------------------------------------------")
                encontrar = True  

            print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]}") 

    if not encontrar:
        print("\n\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("Ainda não existem livros para esse género.")


def contar_livro_genero():

    contador_romance = 0
    contador_ficcao = 0
    contador_fantasia = 0
    contador_terror = 0
    contador_poesia = 0

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  
         
        genero_livro = campos[2] 
        
        if genero_livro == "Romance":
            contador_romance += 1
        elif genero_livro == "Ficção":
            contador_ficcao += 1
        elif genero_livro == "Fantasia":
            contador_fantasia += 1
        elif genero_livro == "Terror":
            contador_terror += 1
        elif genero_livro == "Poesia":
            contador_poesia += 1

    print("--------------------------------------------")
    print("\nNúmero total de livros por género:")
    print("\n")
    print(f"Romance - {contador_romance}")
    print(f"Ficção - {contador_ficcao}")
    print(f"Fantasia - {contador_fantasia}")
    print(f"Terror - {contador_terror}")
    print(f"Poesia - {contador_poesia}")

def menu_function():
    while True:
        print("\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t MENU")
        print("\t 1- Adicionar Livro")
        print("\t 2- Registar Livros")
        print("\t 3- Consultar Livros por Género")
        print("\t 4- Contar livros por Género")
        print("\t 0- Sair")

        menu=input("Opção: ")

        match menu:
            case '1':
                adicionar_livro()
            case '2':
                registar_livros()
            case '3':
                consultar_livro_genero()
            case '4':
                contar_livro_genero()
            case '0':
                print("A sair.")
                break
            case _:
                print("Foi impossível de compreender. Tente novamente.")
                continue
menu_function()