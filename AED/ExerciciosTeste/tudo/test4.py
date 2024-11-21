'''
4. Exercício 4: Maior e Menor Número em uma Lista
Cria uma função que recebe uma lista de números e retorna o maior e o menor número da lista.
'''
listaNum = []
for i in range(5):
    valor = int(input("Indique o {:n}º valor: ".format(i + 1)))
    listaNum.append(valor)

def maiorMenor(listaNum):
    listaMaior = listaNum[0]
    listaMenor = listaNum[0]
    for num in listaNum:
        if num > listaMaior:
            listaMaior = num
        elif num < listaMenor:
            listaMenor = num
    print(f"O menor: {listaMenor} e o maior: {listaMaior}")
    return listaMaior, listaMenor

maiorMenor(listaNum)


