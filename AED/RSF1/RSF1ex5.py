tempoEmSegundos = float(input("Indique o tempo em segundos: "))

horas = int(tempoEmSegundos // 3600)  
resto = tempoEmSegundos % 3600  
minutos = int(resto // 60)  
segundos = int(resto % 60)  

print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
