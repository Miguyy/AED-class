peso=float(input("Peso em kg: "))
altura=float(input("Altura em metros: "))
IMC= peso/(altura**2)

print(f"IMC= %.2f" %(IMC))

if IMC<18.5:
    print("baixo peso")
elif 18.5<IMC and IMC<24.9:
    print("peso normal")
elif 25<IMC and IMC<29.9:
    print("excesso de peso")
elif 30<IMC and IMC<34.9:
    print("obeso I")
elif 35<IMC and IMC<39.9:
    print("obeso II")
elif IMC>=40:
    print("TOTALMENTO OBESO")



