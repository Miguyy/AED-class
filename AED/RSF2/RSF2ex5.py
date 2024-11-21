import random

print("\t\t Jogo Adivinha o Número")

def jogar():
    while True:
        num = random.randint(1, 50)  
        palpite = 0  

        while True:
            palpite += 1
            n1 = int(input("Indique o seu palpite: "))
            if palpite == 11:
                print("Esgotou as tentativas.")
                break  
            if num > n1:
                print("O número é maior.")
            elif num < n1:
                print("O número é menor.")
            else:
                print(f"Acertou em {palpite} tentativas!")
                break  
        
        win = input("Novo jogo (S/N)? ").upper()
        if win == 'N':
            print("Obrigado por jogar!")
            break  
        elif win == 'S':
            continue  
jogar()
