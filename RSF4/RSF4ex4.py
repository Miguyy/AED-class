def countText(texto):
    caracteres = len(texto)
    print("Caracteres: ", caracteres)

    spaces = texto.count(" ")
    print("Espaços: ", spaces)
    
    vogais = texto.count("a") + texto.count("e") + texto.count("i") + texto.count("o") + texto.count("u")
    print("Vogais: ", vogais)
texto = input("Indique um texto: ")
countText(texto)

