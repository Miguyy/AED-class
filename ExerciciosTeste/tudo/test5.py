'''
5. Exercício 5: Somar Números até Zero
Cria uma função que pede ao utilizador para inserir números (usando input()) até que o número inserido seja zero. A função deve retornar a soma de todos os números inseridos.
'''
soma=0
def somaNum_ateZero(soma):
    while True:
        num=int(input("Indique numeros. 0 é a saída: "))
        if num==0:
            break
        soma+=num
    print(f"A soma é: {soma}")
    return soma
somaNum_ateZero(soma)