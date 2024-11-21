nome=input("Indique um nome: ")

pos1=nome.find(" ")
nome1= nome[:pos1]
print(" ", nome1)

pos2=nome.rindex(" ")
nome2= nome[pos2+1:]
print(" ", nome2)