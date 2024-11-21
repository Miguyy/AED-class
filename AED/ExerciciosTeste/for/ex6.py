#Pede ao utilizador um número N e calcula o fatorial de N usando um laço for.

numN=int(input("Indique um numero: "))
fatorial=1
for i in range(1,numN+1): #começa em 0 e termina em n+1, mas como começa em 1 o fatorial, logo é em 1 que se inicia
    fatorial*=i

print(f"Fatorial de {numN} = {fatorial}")