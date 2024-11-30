#Numero: 40230260
#Nome: Miguel Machado

#importar
import os
from datetime import datetime 
sub_pasta = "files"
caminho_arquivo = os.path.join("files", "atividades.txt")
caminho_arquivo2 = os.path.join("files", "progresso.txt") #caminho para os files com o txt


if not os.path.exists(sub_pasta): #ver se está lá
    os.makedirs(sub_pasta)

def consultaDistancia(): #função para ver as distancias
    distancia_pedida = input("Consulta de: ").strip() #pedir ao utilizador

    print("\n\t\tData \t\t  Tempo registado") 
    print("-------------------------------------------------------------")

    encontrou = False #flag para ver onde e que está nos campos

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'atividades.txt' não existe.") #ver se existe
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas: #ver linha a linha
        campos = linha.strip().split(";")
        if len(campos) == 3 and campos[1] == distancia_pedida:
            encontrou = True
            print(f"\t\t {campos[0]} \t\t {campos[2]}")

    if not encontrou:
        print(f"Nenhuma corrida encontrada para a distância {distancia_pedida}.") #se não encontrou então é porque não existe corrida com essa distancia

def melhoresTempos():
    # Distâncias a consultar
    distancias = ['5k', '10k', '21k']

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'atividades.txt' não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for distancia in distancias: #ver nas distancias
        melhor_tempo = None
        melhor_corrida = None

        for linha in linhas:
            campos = linha.strip().split(";")
            if len(campos) == 3 and campos[1] == distancia:
                tempo_corrida = datetime.strptime(campos[2], "%M:%S")
                if melhor_tempo is None or tempo_corrida < melhor_tempo:
                    melhor_tempo = tempo_corrida
                    melhor_corrida = campos

        if melhor_corrida:
            print(f"Melhor tempo para {distancia}: {melhor_corrida[2]} na data {melhor_corrida[0]}")
        else:
            print(f"Nenhuma corrida encontrada para a distância de {distancia}")

def progressoPessal():
    # Lista para armazenar a distância total por mês 
    distancias_por_mes = [0] * 12  # Inicializa com 0 km para cada mês

    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'atividades.txt' não existe.")
        return

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) == 3:
            # Extrair a data e a distância
            data_corrida = campos[0]
            distancia_corrida = campos[1]
            
            # Validar a distância como numérica e a data no formato esperado
            try:
                # Remover a letra 'k' e converter a distância para número float
                distancia_corrida = float(distancia_corrida.replace('k', ''))  
                data_corrida = datetime.strptime(data_corrida, "%Y-%m-%d")
                mes_corrida = data_corrida.month - 1  # Índice 0 para janeiro, 1 para fevereiro, etc.
                
                # Acumular a distância para o mês correspondente
                distancias_por_mes[mes_corrida] += distancia_corrida
            except:
                continue  # Ignorar entradas mal formatadas

    # Criar ou sobrescrever o arquivo progresso.txt
    t = open(caminho_arquivo2, "w", encoding="utf-8")

    # Escrever as distâncias por mês no arquivo
    t.write("Mês; Distância Total (km)\n")
    for mes in range(12):
        t.write(f"{mes + 1}; {distancias_por_mes[mes]:.2f}\n")
    
    t.close()
    print("Progresso mensal gravado em 'progresso.txt'.")


def menu_function(): #função do menu
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Consulta por distância")
        print("\t 2- Consulta melhores tempos")
        print("\t 3- Gravar progresso")
        print("\t 0- Sair")

        menu=input("Opção: ")

        match menu:
            case '1':
                consultaDistancia()
            case '2':
                melhoresTempos()
            case '3':
                progressoPessal()
            case '0':
                print("A sair do programa")
                break
            case _:
                print("Informação incorrecta. Insira novamente os detalhes.")
                continue
menu_function()







