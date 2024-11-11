palavras=[]

for i in range(5):
    palavrasUtilizador = (input("Indique a {:n}ª palavra: ".format(i + 1)))
    palavras.append(palavrasUtilizador)


print("Lista de palavras:", palavras)


palavra_escolhida = input("Escolha uma palavra da lista: ")

if palavra_escolhida in palavras:
    posicao_palavra = palavras.index(palavra_escolhida)
    print(f"A palavra '{palavra_escolhida}' está na posição {posicao_palavra} da lista.")
else:
    print("A palavra não está na lista.")

letra = input(f"Escolha uma letra da palavra '{palavra_escolhida}': ")

if letra in palavra_escolhida:
    posicao_letra = palavra_escolhida.index(letra)
    print(f"A letra '{letra}' está na posição {posicao_letra} da palavra '{palavra_escolhida}'.")
else:
    print(f"A letra '{letra}' não foi encontrada na palavra '{palavra_escolhida}'.")
