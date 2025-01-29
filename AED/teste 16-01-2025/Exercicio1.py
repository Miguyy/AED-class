# IDENTIFICAÇÃO DO ESTUDANTE    
# Numero : 40230260
# Ñome: Miguel Machado

import random #importar a biblioteca random

def gerar_numero_aleatorio(minimo, maximo, excluidos): #criação da função para gerar numeros aleatorios
    while True: #enquanto for verdade
        numero = random.randint(minimo, maximo) #o numero vai ser random e inteiro
        if numero not in excluidos:  #se o numero não estiver nos excluidos, então vai devolver o numero
            return numero

def analisar_lista(lista): #criação da função para analisar a lista de numeros
    return [num for num in lista if num % 5 == 0 or num % 10 == 0] #vai devolver valores, dentro de uma lista, que sejam divisiveis por 5 e 10

def main(): #criação da função principal
    numeros_gerados = [] #lista para os numeros gerados
    minimo = 1 #tal como o enunciado diz, o minimo vai ser 1 
    maximo = 100 #tal como o enunciado diz, o maximo vai ser 100

    while True: #enquanto for verdade
        numero = gerar_numero_aleatorio(minimo, maximo, numeros_gerados) #o numero vai ser igual à função de gerar numeros (com o random)
        numeros_gerados.append(numero) #a lista vai recolher os numeros gerados e guardar lá
        print(f"Número gerado: {numero}") #imprimir o numero gerado

        if numero == 100: #se o numero for igual a 100, então:
            print("Se o 100 foi gerado, então vai encerrar o programa.") #imprime a dizer que o programa vai ser encerrado
            break #termina o programa

        resposta = input("Deseja gerar um novo número (S/N)? ").strip().upper() #antes de fechar o programa, vai haver uma pergunta para o utilizador
        if resposta == 'N': #se não for para gerar mais, então termina
            break
        elif resposta == 'S': #se for para gerar mais, então continua a partir do menor random possivel
            minimo = numero
        else:
            print("Resposta inválida. A encerrar o programa.") #caso o utiizador resposta incorrectamente, então o programa vai dizer que a resposta foi invalida e vai fechar o mesmo
            break

    numeros_ordenados = sorted(numeros_gerados, reverse=True) #a partir da lista numeros_ordernados, vão ser recolhidos aqueles que foram encontrado e colocar a decrescer
    print("\nLista de números gerados de forma decrescente:", numeros_ordenados)

    divisiveis = analisar_lista(numeros_ordenados) #a variavel vai analisar a lista e vai recolher aqueles (a partir da função anterior), dos numeros divisiveis por 5 e 10 e imprimir os mesmos
    print("Números divisíveis por 5 ou 10:", divisiveis)

main() #fim do loop

