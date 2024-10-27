sexo=str(input("Indique o sexo (M/F): ")) .upper()
idade=int(input("Idade: "))

match sexo:
    case 'F':
        fcm=226-idade
        print(f"FCM= {fcm} bpm")
    case 'M':
        fcm=220-idade
        print(f"FCM= {fcm} bpm")
    case _:
        print("Dados incorrectos")


