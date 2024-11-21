meses=["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro"," Outubro", "Novembro", "Dezembro"]
listaFaturacao=[]

def maiorFaturacao(listaFaturacao):
    maior=max(listaFaturacao)
    pos=listaFaturacao.index(maior)
    return (meses[pos])


def menorFaturacao(listaFaturacao):
    menor=min(listaFaturacao)
    pos=listaFaturacao.index(menor)
    return (meses[pos])

def mediaMensal_Faturacao(listaFaturacao):
    media=sum(listaFaturacao)/len(listaFaturacao)
    return media

for i in range(12):
    faturacao=int(input("Indique a faturacção do mês {}:  ".format(meses[i])))
    listaFaturacao.append(faturacao)

print("Mês de maior faturação: ", maiorFaturacao(listaFaturacao))
print("Mês de menor faturação: ", menorFaturacao(listaFaturacao))
print("Valor médio: ", mediaMensal_Faturacao(listaFaturacao))



