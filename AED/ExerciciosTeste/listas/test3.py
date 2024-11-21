'''
Exercício 3: Listar Números Primos de uma Lista
Enunciado:
Dada uma lista de números, escreve um programa que selecione apenas os números primos da lista.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função para verificar se o número é primo
def verSePrimo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Filtrando os números primos da lista
primos = [num for num in lista if verSePrimo(num)]

# Imprimindo os números primos
print("Primos:", primos)
