import os
from datetime import datetime

# Configuração do caminho do ficheiro
sub_pasta = "files"
caminho_arquivo = os.path.join("files", "corridas2.txt")

# Garantir que a pasta existe
if not os.path.exists(sub_pasta):
    os.makedirs(sub_pasta)

# Função para mostrar todas as corridas
def listar_corridas():
    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas2.txt' não existe.")
        return

    print("\t\t\t Data \t\t Distância (km) \t\t Tempo")
    print("-------------------------------------------------------------")

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    if not linhas:
        print("Nenhuma corrida foi encontrada.")
        return

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3:
            print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]}")

# Função para consultar corridas por distância
def consulta_distancia():
    distancia_pedida = input("Insira a distância da consulta (em km): ").strip()

    print("\n\t\tData \t\t Distância (km) \t\t Tempo")
    print("-------------------------------------------------------------")

    encontrou = False

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas2.txt' não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3 and campos[1] == distancia_pedida:
            encontrou = True
            print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]}")

    if not encontrou:
        print(f"Nenhuma corrida encontrada para a distância {distancia_pedida} km.")

# Função para calcular o melhor tempo para uma distância específica
def melhor_tempo_distancia():
    distancia_escolhida = input("Insira a distância (em km) para verificar o melhor tempo: ")

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas2.txt' não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    melhor_tempo = None
    melhor_corrida = None

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3 and campos[1] == distancia_escolhida:
            tempo_corrida = datetime.strptime(campos[2], "%H:%M:%S")
            if melhor_tempo is None or tempo_corrida < melhor_tempo:
                melhor_tempo = tempo_corrida
                melhor_corrida = campos

    if melhor_corrida:
        print(f"Melhor tempo para {distancia_escolhida} km: {melhor_corrida[2]} na data {melhor_corrida[0]}")
    else:
        print(f"Nenhuma corrida encontrada para a distância de {distancia_escolhida} km.")

# Função para somar as distâncias por mês
def somar_distancias_por_mes():
    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'corridas2.txt' não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    distancias_por_mes = {}

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3:
            data_valida = datetime.strptime(campos[0], "%d/%m/%Y")
            distancia_valida = float(campos[1])
            mes = data_valida.strftime("%Y-%m")
            distancias_por_mes[mes] = distancias_por_mes.get(mes, 0) + distancia_valida

    print("\nDistâncias por mês:")
    for mes, distancia_total in distancias_por_mes.items():
        print(f"{mes}: {distancia_total:.2f} km")

# Função para recriar o ficheiro
def recriar_ficheiro():
    if os.path.isfile(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("O ficheiro 'corridas2.txt' foi apagado.")
    else:
        print("O ficheiro 'corridas2.txt' não existe.")

    t = open(caminho_arquivo, "w", encoding="utf-8")
    t.close()

    print("O ficheiro foi recriado.")

# Menu principal
def menu():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Listar todas as corridas")
        print("\t 2- Consultar corridas por distância")
        print("\t 3- Melhor tempo por distância")
        print("\t 4- Somar distâncias por mês")
        print("\t 5- Recriar o ficheiro")
        print("\t 0- Sair")
        print("\n")
        opcao = input("Opção: ")
        print("\n")

        match opcao:
            case '1':
                listar_corridas()
            case '2':
                consulta_distancia()  # Alterado para consultar por distância
            case '3':
                melhor_tempo_distancia()
            case '4':
                somar_distancias_por_mes()
            case '5':
                recriar_ficheiro()
            case '0':
                print("A sair do programa.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
