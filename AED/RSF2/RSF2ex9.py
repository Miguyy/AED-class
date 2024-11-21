num1 = int(input("Número: "))

if 1 <= num1 <= 99:
    binario = ""
    
    while num1 > 0:
        binario = str(num1 % 2) + binario  
        num1 = num1 // 2  
    print(f"Resultado: {binario}")
else:
    print("Por favor, insira um número entre 1 e 99.")
