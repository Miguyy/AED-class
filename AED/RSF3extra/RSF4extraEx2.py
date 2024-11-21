def countWord():
    texto = input("Texto: ")
    pesquisa = input("Pesquisa: ")

    pos = texto.find(pesquisa)  
    contador = 0 

    while pos != -1: 
        contador += 1 
        print("Ocorre nas posições:", pos) 
        pos = texto.find(pesquisa, pos + 1)  
    return contador  

ocorrencias = countWord()  
print("Número de ocorrências:", ocorrencias)  
