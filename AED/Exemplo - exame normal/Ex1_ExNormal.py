gessList = ['00-CC-00', '01-CC-01', '02-CC-02', '03-CC-03', '04-CC-04','05-CC-05', '06-CC-06', '07-CC-07', '08-CC-08', '09-CC-09']

parkList = []

def parkValidator(matricula, movimento):
    if movimento == "E":  
        if matricula in gessList and matricula not in parkList:
            return True
        else:
            return False
    elif movimento == "S":  
        if matricula in parkList:
            return True
        else:
            return False
    else:
        raise ValueError("Movimento inválido! Use 'E' para entrada ou 'S' para saída.")

def parkManager(matricula, movimento):
    if movimento == "E":
        parkList.append(matricula)
        print(f"Matrícula {matricula} adicionada ao parque.")
    elif movimento == "S":
        parkList.remove(matricula)
        print(f"Matrícula {matricula} removida do parque.")
    print(f"Estado atual do parque: {parkList}")

print("Bem-vindo ao sistema de gestão do parque de estacionamento da ESMAD.")
print("Para sair do programa, insira a matrícula '00-00-00'.")

while True:
    matricula = input(f"Indique uma matrícula da lista autorizada {gessList}: ")
    if matricula == "00-00-00":
        print("A sair do programa...")
        break

    movimento = input("Indique o tipo de movimento (E para entrada, S para saída): ").upper()
    try:
        if parkValidator(matricula, movimento):
            parkManager(matricula, movimento)
        else:
            print("Movimento inválido. Verifique se a matrícula está autorizada ou se o movimento faz sentido.")
    except ValueError:
        print("Houve algum erro. Corrija.")