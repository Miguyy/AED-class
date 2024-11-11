#4. Contagem de Letras numa String
#Pede ao utilizador uma palavra e usa um for para contar quantas vezes cada letra aparece.

palavra=input("Indique uma palavra: ")
contagem={}
for letra in palavra:
    if letra in contagem:
        contagem[letra]+=1
    else:
        contagem[letra]=1
print(f"Cada letra aparece: {contagem} vezes")