import os

sub_pasta = "files"
caminho_texto = os.path.join(sub_pasta, "library.txt")
caminho_bin = os.path.join(sub_pasta, "library.bin")

# Função para adicionar livros
def adicionar_livros():
    print("[Adicionar Livro]")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    status = input("Disponibilidade (Sim/Não): ")
    guardar = input("Guardar como (1- texto, 2- binário): ")

    if not os.path.exists(sub_pasta):
        os.makedirs(sub_pasta)

    # Garantir que o arquivo de texto existe
    if not os.path.isfile(caminho_texto):
        print("O ficheiro 'library.txt' não existe. Vai ser criado.")
        t = open(caminho_texto, "w", encoding="utf-8")
        t.close()

    # Criar o arquivo binário se não existir
    if not os.path.isfile(caminho_bin):
        print("O ficheiro binário 'library.bin' não existe. Vai ser criado.")
        b = open(caminho_bin, "wb")  # Criar o arquivo binário vazio
        b.close()

    # Verificar se o livro já foi adicionado no arquivo de texto
    t = open(caminho_texto, "r", encoding="utf-8")
    linhas = t.readlines()
    t.close()

    linha = f"{titulo};{autor};{ano};{status}\n"

    if guardar == "1":  # Salvar em formato de texto
        for linha_existente in linhas:
            if linha_existente.strip().split(";")[0].lower() == titulo.lower():
                print(f"O título {titulo} já foi adicionado anteriormente.")
                return
        
        t = open(caminho_texto, "a", encoding="utf-8")  # Abrir para adicionar ao final
        t.write(linha)
        t.close()

        print("\nO livro foi adicionado ao ficheiro de texto com sucesso.")

    elif guardar == "2":  # Salvar em formato binário
        b = open(caminho_bin, "ab")  # Abrir em modo binário de adição
        b.write(linha.encode("utf-32"))
        b.close()

        print("\nO livro foi adicionado ao ficheiro binário com sucesso.")

    else:
        print("\nOpção inválida. O livro não foi adicionado.")

def listar_livros():
    print("\t\t Título \t\t Autor \t\t Ano \t\t Status \t\t Forma de guardar")
    print("--------------------------------------------------------------------------------------------------------------------------")

    print("Escolha a fonte: (1- texto, 2- binário)")
    fonte = input("Opção: ")

    if fonte == "1":  # Ler do ficheiro de texto
        if not os.path.isfile(caminho_texto):
            print("O ficheiro de texto não existe.")
            return

        t = open(caminho_texto, "r", encoding="utf-8")
        linhas = t.readlines()
        t.close()

        if not linhas:
            print("Não há livros registados no ficheiro de texto.")
            return

        for linha in linhas:
            campos = linha.strip().split(";")
            # Verificar se a linha tem o número correto de campos
            if len(campos) == 4:  # Espera-se 4 campos: título, autor, ano e status
                print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]} \t\t {campos[3]}")
            else:
                print("Linha mal formatada, ignorando.")

    elif fonte == "2":  # Ler do ficheiro binário
        if not os.path.isfile(caminho_bin):
            print("O ficheiro binário não existe.")
            return

        b = open(caminho_bin, "rb")  # Abrir para leitura binária
        dados_binarios = b.read()
        b.close()

        if not dados_binarios:
            print("Não há livros registados no ficheiro binário.")
            return

        livros = dados_binarios.decode("utf-32").split("\n")
        for livro in livros:
            campos = livro.strip().split(";")
            # Verificar se a linha tem o número correto de campos
            if len(campos) == 4:  # Espera-se 4 campos: título, autor, ano e status
                print(f"\t\t {campos[0]} \t\t {campos[1]} \t\t {campos[2]} \t\t {campos[3]}")
            else:
                print("Linha mal formatada, ignorando.")

    else:
        print("Opção inválida.")

def relatorio():
    contador_total_livros = 0
    contador_status_sim = 0
    contador_status_nao = 0

    print("Escolha a fonte para o relatório: (1- texto, 2- binário)")
    fonte = input("Opção: ")

    if fonte == "1":  # Gerar relatório a partir do arquivo de texto
        if not os.path.isfile(caminho_texto):
            print("O ficheiro de texto não existe.")
            return

        t = open(caminho_texto, "r", encoding="utf-8")
        linhas = t.readlines()
        t.close()

        for linha in linhas:
            campos = linha.strip().split(";")
            # Verificar se a linha tem o número correto de campos
            if len(campos) == 4:  # Espera-se 4 campos: título, autor, ano e status
                contador_total_livros += 1
                status = campos[3].strip().lower()
                if status == "sim":
                    contador_status_sim += 1
                elif status == "não":
                    contador_status_nao += 1
            else:
                print("Linha mal formatada, ignorando.")

        print(f"Livros Total: {contador_total_livros}")
        print(f"Livros Disponíveis: {contador_status_sim}")
        print(f"Livros Indisponíveis: {contador_status_nao}")

    elif fonte == "2":  # Gerar relatório a partir do arquivo binário
        if not os.path.isfile(caminho_bin):
            print("O ficheiro binário não existe.")
            return

        b = open(caminho_bin, "rb")  # Abrir para leitura binária
        dados_binarios = b.read()
        b.close()

        if not dados_binarios:
            print("Não há livros registados no ficheiro binário.")
            return

        livros = dados_binarios.decode("utf-32").split("\n")
        for livro in livros:
            campos = livro.strip().split(";")
            # Verificar se a linha tem o número correto de campos
            if len(campos) == 4:  # Espera-se 4 campos: título, autor, ano e status
                contador_total_livros += 1
                status = campos[3].strip().lower()
                if status == "sim":
                    contador_status_sim += 1
                elif status == "não":
                    contador_status_nao += 1
            else:
                print("Linha mal formatada, ignorando.")

        print(f"Livros Total: {contador_total_livros}")
        print(f"Livros Disponíveis: {contador_status_sim}")
        print(f"Livros Indisponíveis: {contador_status_nao}")

    else:
        print("Opção inválida.")


# Função principal do menu
def menu_function():
    while True:
        print("\n")
        print("----------------------------------------")
        print("\t\t MENU")
        print("\t 1- Adicionar livro")
        print("\t 2- Listar livros")
        print("\t 3- Gerar relatório")
        print("\t 0- Sair")
        print("\n")
        menu = input("Opção: ")

        match menu:
            case '1':
                adicionar_livros()
            case '2':
                listar_livros()
            case '3':
                relatorio()
            case '0':
                print("A sair do programa")
                break
            case _:
                print("Informação incorrecta. Insira novamente os detalhes.")
                continue

menu_function()
