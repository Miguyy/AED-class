import os
from datetime import datetime

# Configuração do caminho do ficheiro
sub_pasta = "files"
caminho_arquivo = os.path.join("files", "corridas.txt")

# Garantir que a pasta existe
if not os.path.exists(sub_pasta):
    os.makedirs(sub_pasta)

# Função para validar entrada de data
def validar_data(data):
    try:
        return datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return None

# Função para validar tempo (HH:MM:SS)
def validar_tempo(tempo):
    try:
        return datetime.strptime(tempo, "%H:%M:%S")
    except ValueError:
        return None

# Função para validar distância
def validar_distancia(distancia):
    try:
        return float(distancia)
    except ValueError:
        return None

# Função para adicionar uma corrida ao ficheiro
def adicionar_corrida():
    data = input("Insira a data da corrida (formato DD/MM/AAAA): ")
    data_valida = validar_data(data)
    if not data_valida:
        print("Erro: Data inválida. Tente novamente.")
        return

    distancia = input("Insira a distância da corrida (em km): ")
    distancia_valida = validar_distancia(distancia)
    if distancia_valida is None:
        print("Erro: Distância inválida. Tente novamente.")
        return

    tempo = input("Insira o tempo da corrida (formato HH:MM:SS): ")
    tempo_valido = validar_tempo(tempo)
    if not tempo_valido:
        print("Erro: Tempo inválido. Tente novamente.")
        return

    # Criar o ficheiro se não existir
    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas.txt' não existe. Vai ser criado.")
        with open(caminho_arquivo, "w", encoding="utf-8") as t:
            pass

    # Adicionar a nova corrida ao ficheiro
    with open(caminho_arquivo, "a", encoding="utf-8") as t:
        linha = f"{data};{distancia};{tempo}\n"
        t.write(linha)

    print("A corrida foi adicionada com sucesso.")

# Função para mostrar todas as corridas
def listar_corridas():
    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas.txt' não existe.")
        return

    print("\t\t\t Data \t\t Distância (km) \t\t Tempo")
    print("-------------------------------------------------------------")

    with open(caminho_arquivo, "r", encoding="utf-8") as t:
        linhas = t.readlines()

    if not linhas:
        print("Nenhuma corrida foi encontrada.")
        return

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3:
            print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]}")

# Função para consultar corridas por data
def consulta_data():
    data_pedida = input("Insira a data da consulta (formato DD/MM/AAAA): ").strip()
    # Valida se a data inserida é válida
    data_valida = validar_data(data_pedida)
    if not data_valida:
        print("Erro: Data inválida. Tente novamente.")
        return

    print("\n\t\tData \t\t Distância (km) \t\t Tempo")
    print("-------------------------------------------------------------")

    encontrou = False

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas.txt' não existe.")
        return

    with open(caminho_arquivo, "r", encoding="utf-8") as t:
        linhas = t.readlines()

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3:
            data_corrida = campos[0]
            if data_corrida == data_pedida:
                encontrou = True
                print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]}")

    if not encontrou:
        print(f"Nenhuma corrida encontrada para a data {data_pedida}.")

# Função para calcular o melhor tempo para uma distância específica
def melhor_tempo_distancia():
    distancia_escolhida = input("Insira a distância (em km) para verificar o melhor tempo: ")
    distancia_valida = validar_distancia(distancia_escolhida)
    if distancia_valida is None:
        print("Erro: Distância inválida. Tente novamente.")
        return

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas.txt' não existe.")
        return

    with open(caminho_arquivo, "r", encoding="utf-8") as t:
        linhas = t.readlines()

    melhor_tempo = None
    melhor_corrida = None

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3 and validar_distancia(campos[1]) == distancia_valida:
            tempo_corrida = validar_tempo(campos[2])
            if tempo_corrida and (melhor_tempo is None or tempo_corrida < melhor_tempo):
                melhor_tempo = tempo_corrida
                melhor_corrida = campos

    if melhor_corrida:
        print(f"Melhor tempo para {distancia_escolhida} km: {melhor_corrida[2]} na data {melhor_corrida[0]}")
    else:
        print(f"Nenhuma corrida encontrada para a distância de {distancia_escolhida} km.")

# Função para somar as distâncias por mês
def somar_distancias_por_mes():
    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas.txt' não existe.")
        return

    with open(caminho_arquivo, "r", encoding="utf-8") as t:
        linhas = t.readlines()

    distancias_por_mes = {}

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3:
            data_valida = validar_data(campos[0])
            distancia_valida = validar_distancia(campos[1])
            if data_valida and distancia_valida is not None:
                mes = data_valida.strftime("%Y-%m")
                distancias_por_mes[mes] = distancias_por_mes.get(mes, 0) + distancia_valida

    print("\nDistâncias por mês:")
    for mes, distancia_total in distancias_por_mes.items():
        print(f"{mes}: {distancia_total:.2f} km")

# Função para recriar o ficheiro
def recriar_ficheiro():
    if os.path.isfile(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("O ficheiro 'corridas.txt' foi apagado.")
    else:
        print("O ficheiro 'corridas.txt' não existe.")

    with open(caminho_arquivo, "w", encoding="utf-8") as t:
        pass

    print("O ficheiro foi recriado.")

# Menu principal
def menu():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Adicionar corrida")
        print("\t 2- Listar todas as corridas")
        print("\t 3- Consultar corridas por data")
        print("\t 4- Melhor tempo por distância")
        print("\t 5- Somar distâncias por mês")
        print("\t 6- Recriar o ficheiro")
        print("\t 0- Sair")
        print("\n")
        opcao = input("Opção: ")
        print("\n")

        match opcao:
            case '1':
                adicionar_corrida()
            case '2':
                listar_corridas()
            case '3':
                consulta_data() #data/distancia
            case '4':
                melhor_tempo_distancia()
            case '5':
                somar_distancias_por_mes()
            case '6':
                recriar_ficheiro()
            case '0':
                print("A sair do programa.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
