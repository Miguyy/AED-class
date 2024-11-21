def standardName():
    nome = input("Nome: ")
    pos1 = nome.find(" ")
    primeiro_nome = nome[:pos1]
    pos2 = nome.rindex(" ")
    ultimo_nome = nome[pos2+1:]
    
    iniciais = ""
    for nome_intermediario in nome[pos1+1:pos2].split():
        iniciais += nome_intermediario[0].upper() + ". "

    nome_normalizado = print(f"{primeiro_nome} {iniciais}{ultimo_nome}")
    print(nome_normalizado)

standardName()
