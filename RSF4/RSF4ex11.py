def printCharLine(texto, numeroCar):
    for i in range(0, len(texto), numeroCar):
        print(texto[i:i + numeroCar]) 
texto = input("Escreve aqui: ")
numeroCar = 10
printCharLine(texto, numeroCar)
