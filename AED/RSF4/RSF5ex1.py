def aboveAverage(listNum):
    media=sum(listNum)/len(listNum)
    count=0
    for numero in listNum:
        if numero > media:
            count+=1
    return count
listNum=[]
for i in range(10):
    numero=int(input("Indique o {:n}º numero: " .format(i+1)))
    listNum.append(numero)
print("Existem {:n} numeros acima da media.".format(aboveAverage(listNum)))
        

