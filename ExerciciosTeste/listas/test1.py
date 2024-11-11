'''
Exercício 1: Remover Elementos Duplicados
Enunciado:
Dada uma lista de números, escreve um programa que remova todos os elementos duplicados, mantendo apenas a primeira ocorrência de cada número.
'''

lista=[1,2,3,4,1,5,3]

lista2=[]

for num in lista:
    if num not in lista2:
        lista2.append(num)
print(lista2)