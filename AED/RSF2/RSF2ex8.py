num1=int(input("Indique um número:"))
contagem_div=0

for i in range (1,num1):
    if num1 %i==0:
        contagem_div+=i

if contagem_div==num1:
    print(f"O número {num1} é um numero perfeito")
else:
    print(f"O número {num1} não é um numero perfeito")

