numero1=int(input("Indique o limite inferior 1: "))
numero2=int(input("Indique o limite superior 1: "))
numero3=int(input("Indique o limite inferior 2: "))
numero4=int(input("Indique o limite superior 2: "))
soma=0
soma2=0

for i in range(numero1,numero2+1):
    numero1=int(input("Indique o limite inferior 1: "))
    numero2=int(input("Indique o limite superior 1: "))
    if i %2==0:
        soma+=i
for i in range(numero3, numero4+1):
    if i %2!=0:
        soma2+=i


print("A soma de todos os pares entre {:n} e {:n} é {}".format(numero1, numero2, soma))
print("A soma de todos os impares entre {:n} e {:n} é {}".format(numero3, numero4, soma2))
