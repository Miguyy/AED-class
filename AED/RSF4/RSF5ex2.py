import random
def generateNumbers(limInf,limSup,qtNum):
    count=0
    listNum=[]
    while count<qtNum:
        num=random.randint(limInf,limSup)
        if num not in listNum:
            listNum.append(num)
            count+=1
    return listNum

resposta='S'
while resposta.upper() =='S':
    print("Numeros: ", generateNumbers(1,50,5))
    print("Estrelas: ",generateNumbers(1,12,2))
    resposta=input("Gerar nova chave (S/N)?")


