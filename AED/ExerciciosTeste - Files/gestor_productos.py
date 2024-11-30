import os

sub_pasta="files"
caminho_arquivo = os.path.join("files", "inventario.txt")

def adicionar_producto():
    id_producto=input("Indique o ID do produto: ")
    nome_producto=input("Indique o nome do producto: ")
    quantidade=input("Indique a quantidade: ")
    preco_unitário=(input("Indique o preço unitário: "))

    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'inventario.txt' não existe. Vai ser criado.")
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.close()

    os.system('cls')

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        if linha.strip().split(";")[0].lower() == id_producto.lower():
            print(f"O producto com ID {id_producto} já existe no ficheiro.")
            return
        
    t = open(caminho_arquivo, "a", encoding="utf-8")
    linha = id_producto + ";" + nome_producto + ";" + quantidade + ";" + preco_unitário
    t.write(linha + "\n")
    t.close()

    print("O producto foi adicionado com sucesso.")

def registar_producto():

    print("\t\t\t ID do producto \t\t\t Nome do producto \t\t\t Quantidade \t\t\t Preço unitário")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    os.system('cls')
    encontrar = False
    
    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines() 
    t.close()
    
    for linha in linhas:
        campos = linha.strip().split(";") 
        if len(campos)==4:
            print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]} \t\t {campos[3]}")
            encontrar=True
    if not encontrar:
        print("\n\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("Nenhum producto foi encontrado.")


def consultar_nome_producto():
    nome_producto = input("Indique o nome do producto: ")
    os.system('cls')
    encontrar = False  

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  

        if campos[1] ==nome_producto:  
            if not encontrar:  
                print("\t\t\t ID do producto \t\t\t Nome do producto \t\t\t Quantidade \t\t\t Preço unitário")
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                encontrar = True  

            print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]} \t\t {campos[3]}")

    if not encontrar:
        print("\n\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("Ainda não existem productos com esse nome.")

def actualizar_quantidade_producto():
    id_producto = input("Indique o ID do producto: ")
    nova_quantidade_producto = input(f"Indique a nova quantidade do producto com o ID {id_producto}: ")
    os.system('cls')
    encontrar = False  
    linhas_atcualizadas = []  

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  
        if campos[0] == id_producto: 
            campos[2] = nova_quantidade_producto 
            encontrar = True
        linhas_atcualizadas.append(";".join(campos))

    if encontrar:
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.writelines("\n".join(linhas_atcualizadas) + "\n")  
        t.close()
        print(f"\nQuantidade do producto com ID {id_producto} atualizada com sucesso!")
    else:
        print("Erro: Producto não encontrado.")

def remover_producto():
    id_producto = input("Indique o ID do producto a remover: ")
    os.system('cls')
    encontrar = False  
    linhas_restantes = []  

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  
        if campos[0] == id_producto: 
            encontrar = True
            print(f"Producto com ID {id_producto} removido com sucesso.")
        else:
            linhas_restantes.append(linha)
    if encontrar:
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.writelines(linhas_restantes)  
        t.close()
    else:
        print("Erro: Producto não encontrado.")


def consultar_valorTotal_inventario():
    total=0
    listaPrecos=[]
    os.system('cls')
    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()
    
    for linha in linhas:
        campos = linha.strip().split(";")  
        quantidade = int(campos[2]) 
        preco_unitario = float(campos[3])  
        total += quantidade * preco_unitario
        listaPrecos.append(preco_unitario)
    if listaPrecos:
        preco_unitario_min=min(listaPrecos)
        preco_unitario_max=max(listaPrecos)
        preco_unitario_media=sum(listaPrecos)/len(listaPrecos)

    print(f"O valor total é: {total:.2f}")
    print("\n")
    print(f"O maior valor foi de {preco_unitario_min:.2f}")
    print("\n")
    print(f"O menor valor foi de {preco_unitario_max:.2f}")
    print("\n")
    print(f"A média foi de {preco_unitario_media:.2f}")

def menu_function():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Adicionar producto")
        print("\t 2- Registar todos os productos ")
        print("\t 3- Consultar producto pelo nome")
        print("\t 4- Actualizar a quantidade do producto ")
        print("\t 5- Remover o producto")
        print("\t 6- Consultar o valor total do inventário ")
        print("\t 0- Sair")
        print("\n")
        menu=input("Opção: ")
        print("\n")

        match menu:
            case '1':
                adicionar_producto()
            case '2':
                registar_producto()
            case '3':
                consultar_nome_producto()
            case '4':
                actualizar_quantidade_producto()
            case '5':
                remover_producto()
            case '6':
                consultar_valorTotal_inventario()
            case '0':
                print("A sair do programa")
                break
            case _:
                print("Informação incorrecta. Insira novamente os detalhes.")
                continue
menu_function()