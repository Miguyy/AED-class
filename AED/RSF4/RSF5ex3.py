def positiveList(listNum):
    novaLista=[]
    for i in range(len(listNum)):
        if listNum[i]>=10:
            novaLista.append(listNum[i])
    return novaLista
listNum=[]
i=0
while i<10:
    try:
        numero=int(input("Indique o {:n}º numero: " .format(i+1)))
        if numero<0 or numero>20:
            raise ValueError()     
    except ValueError():
        print("pontuação deve estar entre 0 e 20")
    except:
        print("insira um valor valido")
    else:
        listNum.append(numero)
        i+=1
print("Pontuações positivas" ,positiveList(listNum))



    
        
   

