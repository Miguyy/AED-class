termos=int(input("\n\n\n\t\t\t\ nº de termos a imprimir: "))

seqTermos=""
if termos>=1:
    seqTermos="0"
if termos >=2:
    seqTermos="0,1"

penTermo=0
ultTermos=1

for i in range (3, termos+1):
    novoTermo=penTermo+ultTermos
    seqTermos+=","+str(novoTermo)
    penTermo=ultTermos
    ultTermos=novoTermo
print(f"primeiros {termos} termos da sequencia fibonacci: {seqTermos}")
