import os

sub_pasta="files"
caminho_arquivo = os.path.join("files", "tarefas.txt")

def adicionar_tarefas():
    print("[Adicionar Tarefa]")
    nome_tarefa=input("Indique o nome da tarefa: ")
    data_tarefa=input("Indique a data de vencimento, no formato (AAAA-MM-DD): ")
    prioridade_tarefa=input("Indique a prioridade (Baixa, Média, Alta): ")
    status_tarefa=input("Indique o status (Pendente, Concluída): ")

    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'tarefas.txt' não existe. Vai ser criado.")
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.close()

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        if linha.strip().split(";")[0].lower() == nome_tarefa.lower():
            print(f"A tarefa com o nome {nome_tarefa} já foi adicionado anteriormente.")
            return
        
    t = open(caminho_arquivo, "a", encoding="utf-8")
    linha = nome_tarefa + ";" + data_tarefa + ";" + prioridade_tarefa + ";" + status_tarefa
    t.write(linha + "\n")
    t.close()

    print("\nA tarefa foi adicionada com sucesso.")

def listar_tarefas():
    print("\t\t Nome da tarefa \t\t Data de vencimento \t\t Prioridade \t\t Status")
    print("--------------------------------------------------------------------------------------------------------------------------")

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines() 
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";") 
        print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]} \t\t {campos[3]}") 

def relatorio():
    contador_prioridade_tarefa_baixa=0
    contador_prioridade_tarefa_media=0
    contador_prioridade_tarefa_alta=0
    contador_status_tarefa_pendente=0
    contador_status_tarefa_concluida=0

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")  
        
        prioridade_tarefa = campos[2] 
        status_tarefa = campos[3] 
        
        if prioridade_tarefa == "Baixa":
            contador_prioridade_tarefa_baixa += 1
        elif prioridade_tarefa == "Média":
            contador_prioridade_tarefa_media += 1
        elif prioridade_tarefa == "Alta":
            contador_prioridade_tarefa_alta += 1
        if status_tarefa == "Pendente":
            contador_status_tarefa_pendente +=1
        elif status_tarefa == "Concluída":
            contador_status_tarefa_concluida +=1

    print("--------------------------------------------")
    print("\n")
    print(f"Tarefa prioridade baixa - {contador_prioridade_tarefa_baixa}")
    print(f"Tarefa prioridade média - {contador_prioridade_tarefa_media}")
    print(f"Tarefa prioridade alta - {contador_prioridade_tarefa_alta}")
    print(f"Pendentes - {contador_status_tarefa_pendente}")
    print(f"Concluídas - {contador_status_tarefa_concluida}")

def menu_function():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Adicionar tarefa")
        print("\t 2- Listar tarefas")
        print("\t 3- Gerar relatório")
        print("\t 0- Sair")
        print("\n")
        menu=input("Opção: ")
        print("\n")

        match menu:
            case '1':
                adicionar_tarefas()
            case '2':
                listar_tarefas()
            case '3':
                relatorio()
            case '0':
                print("A sair do programa")
                break
            case _:
                print("Informação incorrecta. Insira novamente os detalhes.")
                continue
menu_function()