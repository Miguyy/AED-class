#Pede ao utilizador um número e usa um for para verificar se o número é primo.

num = int(input("Digite um número: "))
is_primo = True

# Verificar se o número é menor ou igual a 1
if num <= 1:
    is_primo = False

# Verificar se o número é divisível por algum número entre 2 e num-1
for i in range(2, num):
    if num % i == 0:
        is_primo = False
        break

# Exibir o resultado
if is_primo:
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")
