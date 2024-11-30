import os

# Caminho para o ficheiro de eventos
sub_pasta = "files"
caminho_arquivo = os.path.join(sub_pasta, "eventos.txt")


def adicionar_evento():
    print("[Adicionar Evento]")
    nome_evento = input("Indique o nome do evento: ")
    cidade_evento = input("Indique a cidade do evento: ")
    pais_evento = input("Indique o país do evento: ")
    continente_evento = input("Indique o Continente do evento: ")
    data_evento = input("Indique a data do evento no formato (YYYY-MM-DD): ")
    capacidade_max = input("Indique a capacidade máxima do evento: ")

    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'eventos.txt' não existe. Vai ser criado.")
        t = open(caminho_arquivo, "w", encoding="utf-8")
        t.close()

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        if linha.strip().split(";")[0].lower() == nome_evento.lower():
            print(f"O evento: {nome_evento} já existe no ficheiro.")
            return

    t = open(caminho_arquivo, "a", encoding="utf-8")
    linha = nome_evento + ";" + cidade_evento + ";" + pais_evento + ";" + continente_evento + ";" + data_evento + ";" + capacidade_max + ";0"
    t.write(linha + "\n")
    t.close()

    print("\nO evento foi adicionado com sucesso.")


def inscricao():
    print("[Inscrever Participante]")
    nome_evento = input("Indique o nome do evento: ")
    data_evento = input("Indique a data do evento no formato (YYYY-MM-DD): ")

    if not os.path.isfile(caminho_arquivo):
        print("ERRO: O ficheiro de eventos não existe.")
        return

    encontrado = False
    lista_inscritos = []

    # Abrir o arquivo de eventos para leitura
    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")

        # Verificar se a linha tem 7 campos (nome, cidade, país, continente, data, capacidade_max, inscritos)
        if len(campos) != 7:
            print(f"AVISO: Linha ignorada devido a formato incorreto: {linha.strip()}")
            continue

        nome = campos[0].lower()  # Nome do evento em minúsculas para comparação insensível ao caso
        cidade = campos[1]
        pais = campos[2]
        continente = campos[3]
        data = campos[4]
        capacidade_max = int(campos[5])  # Convertendo para inteiro
        inscritos = int(campos[6])  # Convertendo para inteiro

        # Verificar se o nome do evento e a data coincidem
        if nome == nome_evento.lower() and data == data_evento:
            encontrado = True

            if inscritos >= capacidade_max:
                print(f"ERRO: O evento '{nome_evento}' na data '{data_evento}' já está cheio!")
                return

            # Incrementar o número de inscritos
            inscritos += 1
            campos[6] = str(inscritos)  # Atualizar o número de inscritos

            print(f"Inscrição realizada com sucesso! (Inscritos: {inscritos}/{capacidade_max})")

        # Adicionar a linha (modificada ou não) à lista
        lista_inscritos.append(";".join(campos))

    if not encontrado:
        print(f"ERRO: O evento '{nome_evento}' na data '{data_evento}' não foi encontrado.")
        return

    # Reescrever o arquivo com as informações atualizadas
    t = open(caminho_arquivo, "w", encoding="utf-8")
    for linha in lista_inscritos:
        t.write(linha + "\n")
    t.close()


def listar_eventos():
    print("[Listar Eventos]")
    
    if not os.path.isfile(caminho_arquivo):
        print("ERRO: O ficheiro de eventos não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    if not linhas:
        print("Não há eventos registrados.")
        return

    print("Eventos registrados:")
    for linha in linhas:
        campos = linha.strip().split(";")
        nome = campos[0]
        cidade = campos[1]
        pais = campos[2]
        continente = campos[3]
        data = campos[4]
        capacidade_max = campos[5]
        inscritos = campos[6]
        print(f"Evento: {nome}, Cidade: {cidade}, País: {pais}, Continente: {continente}, Data: {data}, Capacidade: {capacidade_max}, Inscritos: {inscritos}")


def consulta_eventos_continente():
    print("[Consultar Eventos por Continente]")
    continente = input("Indique o continente: ")

    if not os.path.isfile(caminho_arquivo):
        print("ERRO: O ficheiro de eventos não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    eventos_encontrados = 0
    for linha in linhas:
        campos = linha.strip().split(";")
        if campos[3].lower() == continente.lower():
            eventos_encontrados += 1
            nome = campos[0]
            cidade = campos[1]
            pais = campos[2]
            data = campos[4]
            print(f"Evento: {nome}, Cidade: {cidade}, País: {pais}, Data: {data}")

    if eventos_encontrados == 0:
        print(f"Não há eventos registrados no continente {continente}.")


def consulta_estatisticas_continente():
    print("[Consultar Estatísticas por Continente]")
    continente = input("Indique o continente: ")

    if not os.path.isfile(caminho_arquivo):
        print("ERRO: O ficheiro de eventos não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    estatisticas = {}
    for linha in linhas:
        campos = linha.strip().split(";")
        continente_evento = campos[3]
        if continente_evento.lower() == continente.lower():
            pais_evento = campos[2]
            if pais_evento not in estatisticas:
                estatisticas[pais_evento] = 0
            estatisticas[pais_evento] += 1

    if estatisticas:
        print(f"Estatísticas de eventos no continente {continente}:")
        for pais, numero_eventos in estatisticas.items():
            print(f"País: {pais}, Número de eventos: {numero_eventos}")
    else:
        print(f"Não há eventos registrados no continente {continente}.")

def relatorio():
    print("[Gerar Relatório]")

    # Verificar se o arquivo de eventos existe
    if not os.path.isfile(caminho_arquivo):
        print("ERRO: O ficheiro de eventos não existe.")
        return

    # Abrir o arquivo de eventos para leitura
    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    # Verificar se há eventos registrados
    if not linhas:
        print("Não há eventos registrados.")
        return

    # Gerar o relatório com todos os eventos
    print("\nRelatório de Eventos:")
    print("Nome do Evento | Cidade | País | Continente | Data | Capacidade Máxima | Inscritos")
    print("-" * 80)

    for linha in linhas:
        campos = linha.strip().split(";")

        # Verificar se a linha tem o número correto de campos (7 campos)
        if len(campos) != 7:
            print(f"AVISO: Linha ignorada devido a formato incorreto: {linha.strip()}")
            continue

        nome = campos[0]
        cidade = campos[1]
        pais = campos[2]
        continente = campos[3]
        data = campos[4]
        capacidade_max = campos[5]
        inscritos = campos[6]

        # Exibir os dados do evento
        print(f"{nome:<20} | {cidade:<10} | {pais:<10} | {continente:<10} | {data:<10} | {capacidade_max:<18} | {inscritos}")
    
    print("\nRelatório gerado com sucesso.")


def menu_function():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Adicionar evento")
        print("\t 2- Inscrever participante num evento ")
        print("\t 3- Listar todos os eventos")
        print("\t 4- Consultar eventos por Continente ")
        print("\t 5- Consultar estatísticas por Continente")
        print("\t 6- Exportar relatório ")
        print("\t 0- Sair")
        print("\n")
        menu = input("Opção: ")
        print("\n")

        match menu:
            case '1':
                adicionar_evento()
            case '2':
                inscricao()
            case '3':
                listar_eventos()
            case '4':
                consulta_eventos_continente()
            case '5':
                consulta_estatisticas_continente()
            case '6':
                relatorio()
            case '0':
                print("A sair do programa.")
                break
            case _:
                print("Informação incorreta. Insira novamente os detalhes.")
                continue


# Chama a função que executa o menu
menu_function()
