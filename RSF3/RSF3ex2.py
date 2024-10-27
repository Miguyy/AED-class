def maior(*numeros:int):
    max=numeros[0]
    for i in range(len(numeros)):
        if numeros [i]>max:
            max=numeros[i]
    return max
print(maior(10,20,12)) 
print(maior(28,9,7,30)) 

