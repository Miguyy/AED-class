#import random

n = int(input("Quantos números deseja ler?: "))

maior = 0
segMaior = 0

for i in range(n):
    #numero = random.randint(1, 99)
    #print(f"Número: {numero}")
    numero=int(input("Numero:"))

    if numero > maior:
        segMaior = maior  
        maior = numero 
    elif numero > segMaior and numero != maior:
        segMaior = numero

print(f"O segundo maior número é: {segMaior}")
