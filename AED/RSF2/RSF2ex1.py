soma=0
maior=0
i=0
while i<10:
    numero=int(input("Indique o {:n}º numero:" .format(i+1)))
    if numero>20:
        continue
    soma+=numero
    i+=1
    if numero>maior:
        maior=numero
    
print("A média é de: {:n}" .format(soma/10))
print("O maior é: {:n}" .format(maior))


    
