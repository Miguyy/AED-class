#Pede ao utilizador um número N e calcula a soma de todos os números de 1 a N usando um laço for.

n=int(input("Indique um número: "))
soma=0
for i in range(1,n+1):
    soma+=i
print(f"A soma de todos os numeros de 1 a {n} são: {soma}")