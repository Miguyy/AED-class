'''
2. Exercício 2: Fatorial de um Número
Cria uma função que calcula o fatorial de um número inteiro positivo usando um ciclo while. O fatorial de um número n é o produto de todos os números inteiros de 1 a n.
'''

numN=int(input("Indique um numero inteiro positivo: "))
def calcFatorial(numN):
    resultado=1
    if numN<1:
        print("Coloque outro numero.")
        return ValueError
    while numN>1:
        resultado*=numN
        numN-=1
    return resultado
print("O fatorial do numero é: {}".format(calcFatorial(numN)))
