'''
Exercício 6: Criar uma Lista de Pares de Índices e Valores
Enunciado:
Dada uma lista de números, escreve um programa que crie uma nova lista contendo tuplas com o índice e o valor de cada elemento da lista original.
'''

lista=[10,20,30,40]
listaIndice=[]
for i in range(len(lista)):
    listaIndice.append((i,lista[i]))
print(f"Os valores dos indices e valores: {listaIndice} ")