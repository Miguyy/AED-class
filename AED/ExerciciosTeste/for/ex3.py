#Dada uma lista de números, usa um for para calcular o produto de todos os elementos da lista.

lista=[1,2,3]
produto=1

for num in lista:
    produto*=num
print(f"O produto de todos os elementos da lista são: {produto}")