'''
1. Contar números abaixo da média
Exercício: Cria uma função belowAverage que receba uma lista de 10 números inteiros (inseridos pelo utilizador) e devolva quantos desses números estão abaixo da média.

'''

numeros=[]
abaixoMedia=[]

for i in range(10):
    numerosUtilizador = int(input("Indique o {:n}º valor: ".format(i + 1)))
    numeros.append(numerosUtilizador)

def belowAverage(numeros):
    media=sum(numeros)/len(numeros)
    print(f"A média é: {media}")
    for num in numeros:
        if num<media:
            abaixoMedia.append(num)
    print(f"Abaixo da média: {abaixoMedia}")
    return len(abaixoMedia)
print("Total de numeros abaixo da media: ", numeros)
belowAverage(numeros)
    
