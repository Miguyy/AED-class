'''
1. Exercício 1: Números Pares e Ímpares
Cria uma função que recebe uma lista de números e retorna duas listas: uma com os números pares e outra com os números ímpares.
'''

listaNum=[1,2,3,4,5,6,7,8,9]

def numPar_impar(listaNum):
    listaPar=[]
    listaImpar=[]
    for num in listaNum:
        if num %2==0:
            listaPar.append(num)
        else:
            listaImpar.append(num)
    print(f"Os numeros pares são: {listaPar}")
    print(f"Os numeros impares são: {listaImpar}")
    return listaImpar,listaPar
numPar_impar(listaNum)
