num=int((input("Numero:")))
primo=True
for i in range(2, num):
    resto=num%i
    if resto==0:
        primo=False
        break
if primo ==True:
    print(f"o numero {num} é primo")
else:
    print(f"o numero {num} não é primo")



    
    
