sexo=str(input("Indique o sexo (M/F): ")). upper()
altura=int(input("Altura em cm: "))

match sexo:
    case 'F':
        pesoIdeal=(altura-100)-(altura-150)/2
        print("Peso ideal:{:.2f}  'kg'" .format(pesoIdeal))
    case 'M':
        pesoIdeal=(altura-100)-(altura-150)/4
        print("Peso ideal: {:.2f}  kg" .format(pesoIdeal))
    case _:
        print("Dados incorrectos")


