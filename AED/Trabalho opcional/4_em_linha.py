#Importação das librarias de cores, para fazer corresponder às escolhas dos jogadores, ou seja, ser mais visível.
import colorama
from colorama import Fore, Style

''' O objectivo deste desafio, é a criacção do jogo 4 em linha.'''

def criação_tabuleiro():
    """Criação do tabuleiro, com 7x6 espaços, na qual é feita a partir de uma matriz."""
    return [[" " for _ in range(7)] for _ in range(6)] #Devolve a quantidade de espaços, ou seja, como é 7x6, então vão ser devolvidas 7 columns e 6 rows.

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro na cmd do vscode, já com cores."""
    for linha in tabuleiro: #Para cada linha do tabuleiro, vão ser inseridos '|', para fazer a tal divisória
        print("|", end="")
        for celula in linha: #Para preencher as celulas linha a linha, se for com o X (player 1), então preenche a celula com um X amarelo. Caso seja preenchida a celula pelo (Player 2), então esta vai ser preenchida com um O e vermelho.
            if celula == "X":
                print(Fore.YELLOW + "X", end=Style.RESET_ALL + "|")
            elif celula == "O":
                print(Fore.RED + "O", end=Style.RESET_ALL + "|")
            else:
                print(" ", end="|")
        print()
    print(" " + " ".join(str(i) for i in range(7))) #Vai ser imprimido o tabuleiro com as modificações

def verificar_vitoria(tabuleiro, simbolo):
    """Verifica se há 4 em linha"""
    # Verifica linhas 
    for linha in tabuleiro: #Verificação das linhas, ou seja, utilizando a interação, é possível verificar linha a linha e com isso permite ver se encontra o mesmo simbolo após encontrar o primeiro. Ex: 'X' ' ' (não há na linha 1) / 'X' 'X' 'X' 'X' ' ' ' ' ' ' (há na linha 2), logo ganhou
        for col in range(4):
            if all(linha[col + i] == simbolo for i in range(4)):
                return True # Se encontrar uma sequência de 4 símbolos iguais nas linhas, o jogador venceu

    # Verifica colunas 
    for col in range(7): 
        for linha in range(3): #A mesma coisa que as linhas. Permite ver, a partir da interação, se existe 4 em linha. Se não houver nada na linha 1, por exemplo, então vai ver se tem na linha 2 e por aí adiante.
            if all(tabuleiro[linha + i][col] == simbolo for i in range(4)):
                return True # Se encontrar uma sequência de 4 símbolos iguais nas colunas, o jogador venceu

    # Verifica diagonais (cima para baixo)
    for linha in range(3):  
        for col in range(4):  # Verificamos as 4 primeiras colunas, pois a sequência de 4 "X" ou "O" não pode ultrapassar a última coluna (coluna 6)
            # Aqui verificamos se há 4 símbolos consecutivos na diagonal, começando da posição [linha, col]. Para isso, verificamos as 4 posições seguintes, movendo tanto para baixo (linha) como para a direita (col)
            if all(tabuleiro[linha + i][col + i] == simbolo for i in range(4)):
                return True  # Se encontrar uma sequência de 4 símbolos iguais na diagonal, o jogador venceu

    # Verifica diagonais (baixo para cima)
    for linha in range(3, 6):  # Começamos a partir da 4ª linha até à última linha (linha 5) para a verificação da diagonal "de baixo para cima"
        for col in range(4):  # Verificamos as 4 primeiras colunas novamente
            # Aqui verificamos se há 4 símbolos consecutivos na diagonal, começando da posição [linha, col]. Para isso, verificamos as 4 posições seguintes, movendo para cima (linha) e para a direita (col)
            if all(tabuleiro[linha - i][col + i] == simbolo for i in range(4)):
                return True  # Se encontrar uma sequência de 4 símbolos iguais na diagonal, o jogador venceu
    return False

def jogada_valida(tabuleiro, coluna):
    """Verifica se a jogada é válida."""
    return 0 <= coluna < 7 and tabuleiro[0][coluna] == " " #Testagem para ver se o jogador jogou na sua rodada.

def fazer_jogada(tabuleiro, coluna, simbolo):
    """Realiza a jogada colocando o símbolo na coluna especificada."""
    for linha in range(5, -1, -1):
        if tabuleiro[linha][coluna] == " ": #Colocação do simbolo na posição desejada
            tabuleiro[linha][coluna] = simbolo
            return

def tabuleiro_cheio(tabuleiro):
    """Verifica se o tabuleiro está cheio."""
    return all(tabuleiro[0][col] != " " for col in range(7)) #Verificação se o tabuleiro está cheio.

def jogo_quatro_em_linha():
    """Função principal."""
    colorama.init(autoreset=True)
    print(Fore.CYAN + "Bem-vindo/a ao jogo Quatro em Linha!")
    jogador1 = input(Fore.YELLOW + "Escreva o nickname do jogador 1: ") #Está a solicitar o nome e já está a informar que a cor do jogador vai ser amarela.
    jogador2 = input(Fore.RED + "Escreva o nickname do jogador 2: ") #Está a solicitar o nome e já está a informar que a cor do jogador vai ser vermelha.
    simbolos = {jogador1: "X", jogador2: "O"} #Utilização da variavel 'simbolos', para informar o utilizador de que simbolos são.

    tabuleiro = criação_tabuleiro()
    jogador_atual = jogador1

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"{Fore.YELLOW if jogador_atual == jogador1 else Fore.RED}Ronda do {jogador_atual} ({simbolos[jogador_atual]}).")

        # Solicita uma jogada válida
        while True:
            try:
                coluna = int(input(f"{jogador_atual}, escolha uma coluna (0-6): "))
                if jogada_valida(tabuleiro, coluna):
                    break
                else:
                    print(Fore.RED + "Jogada inválida. Tente novamente.")
            except ValueError:
                print(Fore.RED + "Entrada inválida. Insira um número entre 0 e 6.")

        # Realiza a jogada
        fazer_jogada(tabuleiro, coluna, simbolos[jogador_atual])

        # Verifica se o jogador actual venceu
        if verificar_vitoria(tabuleiro, simbolos[jogador_atual]):
            imprimir_tabuleiro(tabuleiro)
            print(Fore.GREEN + f"Parabéns, o/a {jogador_atual} ganhou! ")
            break

        # Verifica se o tabuleiro está cheio (empate)
        if tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print(Fore.BLUE + "O jogo terminou num empate!")
            break

        # Alterna entre jogadores
        jogador_atual = jogador1 if jogador_atual == jogador2 else jogador2 #define qual vai ser o jogador actual da jogada

# Executa o jogo
if __name__ == "__main__":
    jogo_quatro_em_linha() #chama a função principal

''' Anotações: Quando o jogador 2 insere o nickname, o jogo está a "contar(?)" / escreve o primeiro espaço com a cor vermelha, no canto superior esquerdo. Estive a ver e acho que é a biblioteca'''
