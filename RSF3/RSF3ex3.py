def heartRate(fc):
    if fc>=50 and fc<=80:
        return("treino aerobico")
    elif fc>80 and fc<=100:
        return("treino cardiovascular")
    if fc>100 and fc<=120:
        return("treino aerobico ideal")
    elif fc>120 and fc<=140:
        return("treino anaerobico")
    else:
        return("não")
    
fc=int(input("indique a sua fc: "))
print(heartRate(fc))

