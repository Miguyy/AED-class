'''
Exercício 2: Listar Números Pares e Ímpares Separadamente
Enunciado:
Dada uma lista de números, escreve um programa que separe os números pares e ímpares em duas listas diferentes.
'''
lista=[1,2,3,4,5,6,7,8,9]
listaPar=[]
listaImpar=[]

for num in lista:
    if num %2==0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(f"Pares: {listaPar}")
print(f"Impares: {listaImpar}")