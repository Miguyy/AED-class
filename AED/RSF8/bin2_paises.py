import os
import random

sub_pasta = "files"
caminho_arquivo = os.path.join(sub_pasta, "paises1.txt")

def ler_paises():
    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'paises1.txt' não existe.")
        return []

    t = open(caminho_arquivo, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    paises = [linha.strip().split(";")[0] for linha in linhas if linha.strip()]
    return paises

def imprimePais(nome_pais, tentativas_restantes):

    num_revelar = 3 - tentativas_restantes
    revelado = ""
    for i, char in enumerate(nome_pais):
        if i < num_revelar:
            revelado += char
        else:
            revelado += "-"
    return revelado

def jogo_adivinha_o_pais():
    paises = ler_paises()
    if not paises:
        return

    pais_escolhido = random.choice(paises)
    tentativas = 3

    print("Bem-vindo ao jogo 'Adivinha o País!'")
    print("Tenta adivinhar o país. Tens 3 tentativas!")

    while tentativas > 0:
        print("\nDica:", imprimePais(pais_escolhido, tentativas))
        palpite = input(f"Tentativa {4 - tentativas}: Qual é o país? ").strip()

        if palpite.lower() == pais_escolhido.lower():
            print("\nAcertaste")
            break
        else:
            tentativas -= 1
            print("Resposta errada. Tente novamente.")

    if tentativas == 0:
        print(f"\nO país era: {pais_escolhido}. ")
jogo_adivinha_o_pais()
