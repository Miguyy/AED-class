def capicua():
    pergunta=input("Insira um texto: ")
    inverso=pergunta[::-1]

    if pergunta==inverso:
        print(f" {pergunta} é capicua")
    else:
        print(f"{pergunta}não é capicua")  
          
capicua()

'''
def capicua():
    pergunta=input("Insira um texto: ")
    if pergunta [:] ==pergunta[::-1]:
        return True
    else: 
        return False
    if capicua() == True:
        print("é")
    else:
        print("não é")
capicua()
'''