def positiveList(listNum, listNome):
    novaLista=[]
    novaLista2=[]
    for i in range(len(listNum)):
        if listNum[i]>=10:
            novaLista.append(listNum[i])
            novaLista2.append(listNome[i])
    return novaLista,novaLista2
listNum=[]
listNome=[]
i=0
while i<10:
    try:
        nome=input("Indique o {:n}º nome: ".format(i+1))
        numero=int(input("Indique o {:n}º numero: " .format(i+1)))
        if numero<0 or numero>20:
            raise ValueError()     
    except ValueError():
        print("pontuação deve estar entre 0 e 20")
    except:
        print("insira um valor valido")
    else:
        listNum.append(numero)
        listNome.append(nome)
        i+=1
print("Pontuações positivas: " ,positiveList(listNum, listNome))



    
        
   

