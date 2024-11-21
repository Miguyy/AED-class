meses=["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro"," Outubro", "Novembro", "Dezembro"]

def pluviosidadeFunction(pluviosidade):
    pluviosidade2=pluviosidade.copy()
    pluviosidade2.sort(reverse=True)
    print("Meses \t Pluviosidade")
    for i in range(12):
        pos=pluviosidade.index(pluviosidade2[i])
        print(meses[pos],"\t", pluviosidade2[i])

pluviosidade=[]
for i in range(12):
    pluviosidade.append(int(input("Pluviosidade no mês de {}: ".format(meses[i]))))
pluviosidadeFunction(pluviosidade)
