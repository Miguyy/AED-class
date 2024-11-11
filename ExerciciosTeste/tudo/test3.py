'''
3. Exercício 3: Contar Vogais
Cria uma função que recebe uma string e retorna o número de vogais (a, e, i, o, u) presentes na string.
'''



'''
texto=input("Indique um texto: ")

def contarVogais(texto):
    vogais=texto.count("a")+texto.count("e")+texto.count("i")+texto.count("o")+texto.count("u")
    print(f"Vogais: {vogais}")
contarVogais(texto)
'''

#ou
texto=input("Indique um texto: ")
def contarVogais(texto):
    vogais=0
    for letra in texto:
        if letra.lower() in 'aeiou':
            vogais+=1
    print(f"Vogais: {vogais}")
    return vogais
contarVogais(texto)

