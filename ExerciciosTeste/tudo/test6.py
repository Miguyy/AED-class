'''
6. Exercício 6: Lista de Quadrados
Cria uma função que recebe um número n e retorna uma lista com os quadrados de todos os números de 1 até n.
'''

numN=int(input("Indique um número: "))

def listaQuad(numN):
    quadrados=[]
    for i in range(1,numN+1):
        quadrados.append(i**2)
    print(f"Os quadrados são: {quadrados}")
    return quadrados
listaQuad(numN)