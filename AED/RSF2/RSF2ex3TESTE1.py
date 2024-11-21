numero1=int(input("Indique o limite inferior: "))
numero2=int(input("Indique o limite superior: "))
soma=0

for i in range(numero1,numero2+1):
    if i %2!=0:
        soma+=i
print("A soma de todos os impares entre {:n} e {:n} é {}".format(numero1, numero2, soma))
