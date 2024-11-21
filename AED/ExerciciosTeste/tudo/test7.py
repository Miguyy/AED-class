'''
7. Exercício 7: Palíndromos
Cria uma função que recebe uma string e retorna True se a string for um palíndromo (uma palavra que é igual quando lida de trás para frente), e False caso contrário.
'''

palavra=input("Indique uma palavra: ")

def capicua(palavra):
    if palavra==palavra[::-1]:
        print("É capicua")
        return True
    else:
        print("Não é capicua")
        return False
capicua(palavra)