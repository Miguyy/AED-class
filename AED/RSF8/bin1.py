import os 

sub_pasta = "files"
caminho_arquivo = os.path.join(sub_pasta, "dados.bin")

def escreveTexto():
    texto_utilizador = input("Indique um texto: ")
    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    t = open(caminho_arquivo, "wb")  
    texto_binario = bytes(texto_utilizador, encoding="utf-32")
    t.write(texto_binario)
    t.close()

    print("Texto gravado com sucesso no ficheiro binário.")
escreveTexto()

def lerTexto():
    if not os.path.isfile(caminho_arquivo):
        print("O ficheiro 'dados.bin' não existe.")
        return

    t = open(caminho_arquivo, "rb")  
    texto_binario = t.read()
    t.close()
    return str(texto_binario, encoding="utf-32")

    '''
    print("\nO que está no ficheiro .bin será apresentado aqui:")
    print(f"Binário: {texto_binario}")
    print(f"Como texto: {texto_binario.decode('utf-32')}")
    '''
lerTexto()
