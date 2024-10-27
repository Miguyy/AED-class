print("Planetas")
print("1- Mercúrio")
print("2- Vénus")
print("3- Marte")
print("4- Júpiter")
print("5- Saturno")
print("6- Urano")

peso=float(input("Indique o seu peso em kg: "))
codigo=int(input("Indique o código: "))

match codigo:
    case 1:
        pesoPlaneta= (peso*0.37)/0.98
        print("O teu peso nesse planeta seria: {:.2}" .format(pesoPlaneta))
    case 2:
        pesoPlaneta= (peso*0.90)/0.98
        print("O teu peso nesse planeta seria: {:.2}" .format(pesoPlaneta))
    case 3:
        pesoPlaneta= (peso*0.37)/0.98
        print("O teu peso nesse planeta seria: {:.2}" .format(pesoPlaneta))
    case 4:
        pesoPlaneta= (peso*2.53)/0.98
        print("O teu peso nesse planeta seria: {:.2}" .format(pesoPlaneta))
    case 5:
        pesoPlaneta= (peso*1.09) /0.98
        print("O teu peso nesse planeta seria: {:.2}" .format(pesoPlaneta))
    case 6:
        pesoPlaneta= (peso*0.91)/0.98
        print("O teu peso nesse planeta seria: {:.2}" .format(pesoPlaneta))
    case _:
        print("refaz")

