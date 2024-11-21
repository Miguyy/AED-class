import random

print("jogo adivinha o numero")

num=random.randint(1,50)
palpite=0


while True:
    palpite+=1
    n1 =int(input("Indique o seu palpite: "))
    if palpite==11:
        print("Esgotou as tentativas")
        break
    if num>n1:
        print("O numero é maior")
    elif num<n1:
        print("o numero é menor")
    else:
        print(f"acertou em {palpite} tentivas ")
        break
    


    
    



