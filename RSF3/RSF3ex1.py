num1=int(input("Escreva 1 numero: "))
num2=int(input("Escreva 1 numero: "))
def somatorio(num1,num2):
    soma=0
    for i in range(num1,num2+1):
        soma+=i
    print(f"soma: {soma}")         
somatorio(num1,num2)

    
    