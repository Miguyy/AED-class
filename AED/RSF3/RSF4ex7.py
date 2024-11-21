def shortName():
   nome=input("Nome: ")
   pos1=nome.find(" ")
   nome1= nome[:pos1]
   pos2=nome.rindex(" ")
   nome2= nome[pos2+1:]
   print(" ", nome1, nome2)
shortName()