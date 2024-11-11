listaNum_n=[]
numN=int(input(("Indique um numero: ")))

for i in range(numN):
    numero=int(input("Indique o {:n}º numero: " .format(i+1)))
    listaNum_n.append(numero)
print("Lista do utilizador: ",listaNum_n)
    
listaNum_n2=[]

def ordenadorLista_dup(listaNum_n):
    for numero in listaNum_n:
        if numero not in listaNum_n2:
            listaNum_n2.append(numero)
    print("Lista do utilizador sem duplicados: ",listaNum_n2)
ordenadorLista_dup(listaNum_n)
    

    
    
