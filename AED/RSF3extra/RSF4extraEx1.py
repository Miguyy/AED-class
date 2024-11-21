def romanNatural():
    num=int(input("Indique um Número entre 1 e 999: "))
    if num<1 or num>999:
        print("Fora do intervalo")
        return
    numRoman=" "
    match num//100:
        case 1:
            numRoman+="C"
        case 2:
            numRoman += "CC"
        case 3:
            numRoman += "CCC"
        case 4:
            numRoman += "CD"
        case 5:
            numRoman += "D"
        case 6:
            numRoman += "DC"
        case 7:
            numRoman += "DCC"
        case 8:
            numRoman += "DCCC"
        case 9:
            numRoman += "CM"
    
    match (num%100)//10:
        case 1:
            numRoman+="XX"
        case 2:
            numRoman += "XXX"
        case 3:
            numRoman += "XL"
        case 4:
            numRoman += "L"
        case 5:
            numRoman += "LX"
        case 6:
            numRoman += "LXX"
        case 7:
            numRoman += "LXXX"
        case 8:
            numRoman += "XC"
        case 9:
            numRoman += "C"

    match num % 10:
        case 1:
            numRoman += "I"
        case 2:
            numRoman += "II"
        case 3:
            numRoman += "III"
        case 4:
            numRoman += "IV"
        case 5:
            numRoman += "V"
        case 6:
            numRoman += "VI"
        case 7:
            numRoman += "VII"
        case 8:
            numRoman += "VIII"
        case 9:
            numRoman += "IX"
            
    print("O numero em romando é: {}" .format(numRoman))
romanNatural()
        
    
        
    
