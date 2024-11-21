numero=1
while numero<=10:
    print(numero)
    numero +=1

numero1=int(input("Indique um numero entre [0-20]: "))

while numero1 <= 0 or numero1 >20:
    print("Indicou um numero invalido. Tente novamente!\n")
    numero1=int(input("Indique um numero entre [0-20]: "))

tabuada=int(input("Imprimir a tabuada dos: "))
numero2=1
while numero2<11:
    print("{:n} * {:n} - {:n}" .format(tabuada, numero2, tabuada*numero))
    numero+=1

import random # biblioteca que permite gerar numeros aleatoriamente

numeroGerado=random.randint(0,20) # gera um nº inteito entre 0 e 20
# inclui os limites inferior e superior
palpite = int(input("Indique o seu palpite:"))
while numeroGerado != palpite:
    print("Não acertou! : ( tente novamente!\n")
    palpite = int(input("Indique o seu palpite:")) 

