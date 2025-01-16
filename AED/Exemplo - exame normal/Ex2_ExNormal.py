from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
from tkinter import messagebox   # messagebox
import os                        # Para manipular ficheiros e caminhos

# Função para carregar as bandas do ficheiro
def lerBandas():
    caminho_bandas = os.path.join("files", "bandas.txt")  # Caminho do ficheiro
    try:
        bandas = open(caminho_bandas).readlines()  # Lê todas as linhas
        lstboxBandas.delete(0, END)  # Limpa a lista
        for banda in bandas:
            lstboxBandas.insert(END, banda.strip())  # Adiciona ao Listbox
    except FileNotFoundError:
        messagebox.showerror("Erro", "Ficheiro 'bandas.txt' não encontrado na pasta 'files'.")

# Função para mostrar músicas da banda selecionada no TreeView
def mostrarMusicas():
    banda_selecionada = lstboxBandas.get(ACTIVE)
    if not banda_selecionada:
        messagebox.showwarning("Aviso", "Selecione uma banda.")
        return

    caminho_musicas = os.path.join("files", "musicas.txt")
    tree.delete(*tree.get_children())  # Limpa o TreeView
    try:
        linhas = open(caminho_musicas).readlines()  # Lê todas as linhas
        for linha in linhas:
            campos = linha.split(";")
            if campos[0] == banda_selecionada:
                tree.insert("", END, values=(campos[1], campos[2]))
    except FileNotFoundError:
        messagebox.showerror("Erro", "Ficheiro 'musicas.txt' não encontrado na pasta 'files'.")

# Função para adicionar uma nova música ao ficheiro de músicas
def adicionarMusica():
    banda_selecionada = lstboxBandas.get(ACTIVE)
    musica = txtMusica.get()
    visualizacoes = txtVisualizacoes.get()

    if not banda_selecionada:
        messagebox.showwarning("Aviso", "Selecione uma banda.")
        return
    if not musica or not visualizacoes:
        messagebox.showwarning("Aviso", "Insira valores válidos.")
        return

    caminho_musicas = os.path.join("files", "musicas.txt")
    try:
        file = open(caminho_musicas, "a")
        file.write(f"{banda_selecionada};{musica};{visualizacoes}; \n")
        file.close()
        messagebox.showinfo("Sucesso", "Música adicionada com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao escrever no ficheiro: {e}")

# Função para mostrar informações adicionais da banda
def verMaisInfo():
    banda_selecionada = lstboxBandas.get(ACTIVE)
    if not banda_selecionada:
        messagebox.showwarning("Aviso", "Por favor, selecione uma banda.")
        return

    caminho_musicas = os.path.join("files", "musicas.txt")
    num_musicas = 0
    musica_mais_vista = ""
    max_visualizacoes = 0
    link = ""

    try:
        linhas = open(caminho_musicas).readlines()
        for linha in linhas:
            campos = linha.split(";")  # Usa o separador correto
            if len(campos) == 4 and campos[0] == banda_selecionada:
                num_musicas += 1

                # Processar visualizações com sufixo 'M' ou 'm'
                visualizacoes_raw = campos[2].strip()
                if visualizacoes_raw.endswith("M"):  # Milhões
                    visualizacoes = int(float(visualizacoes_raw[:-1]) * 1_000_000)
                elif visualizacoes_raw.endswith("m"):  # Milhares
                    visualizacoes = int(float(visualizacoes_raw[:-1]) * 1_000)
                else:
                    continue  # Ignorar valores inválidos

                # Comparar visualizações para encontrar a mais vista
                if visualizacoes > max_visualizacoes:
                    max_visualizacoes = visualizacoes
                    musica_mais_vista = campos[1]  # Nome da música
                    link = campos[3]  # Link do YouTube

        # Atualiza os campos no UI
        txtNumFilmes.delete(0, END)
        txtMaisVisto.delete(0, END)
        txtLink.delete(0, END)

        txtNumFilmes.insert(0, str(num_musicas))
        txtMaisVisto.insert(0, musica_mais_vista)
        txtLink.insert(0, link)
    except FileNotFoundError:
        messagebox.showerror( "Não é possivel encontrar o ficheiro 'musicas.txt'.")
    
# Função para selecionar uma imagem e renderizá-la no canvas
def selecionarImagem():
    caminho_imagem = filedialog.askopenfilename(initialdir="files", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if caminho_imagem:
        img = PhotoImage(file=caminho_imagem)
        canvas.img = img  # Evita que o garbage collector apague a imagem
        canvas.create_image(0, 0, anchor=NW, image=img)

# ---------------Main-------------------------------------------
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Músicas Playlist')

# Bandas 
lbBandas = Label(window, text = "Bandas", font = ("Helvetica", "11"))
lbBandas.place(x=27, y=40)

lstboxBandas = Listbox(window, width=20, height = 11, bd = 4, relief = "sunken")
lstboxBandas.place (x=20, y=70)

# Button para mostrar músicas da banda
btn1 = Button(window, text = ">", width = 6, height = 2, command=mostrarMusicas)
btn1.place(x=160, y=130)

# TreeView para mostrar as músicas da banda selecionada
tree = ttk.Treeview(window, columns = ("Música", "Visualizações"), show = "headings", height = 8, selectmode = "browse")
tree.column("Música", width = 220, anchor = "w")
tree.column("Visualizações", width = 130, anchor = "c")
tree.heading("Música", text = "Música")
tree.heading("Visualizações", text = "Visualizações")
tree.place(x=230, y=70)

# Painel para adicionar música
panel1 = PanedWindow(window, width = 310, height = 180, bd = "3", relief = "sunken" )
panel1.place(x=630, y=70)

lbMusica = Label(panel1, text = "Música", font = ("Helvetica", "10"))
lbVisual = Label(panel1, text = "Visualizações", font = ("Helvetica", "10"))
lbMusica.place(x=10, y=20)
lbVisual.place(x=10, y=70)

txtMusica = Entry(panel1, width=25)
txtVisualizacoes = Entry(panel1, width=15)
txtMusica.place(x=130, y=20)
txtVisualizacoes.place(x=130, y=70)

imgAdicionar = PhotoImage(file=".\\AED\\Exemplo - exame normal\\images\\adicionar.png")  # Atualize o caminho conforme necessário
imgRefresh = PhotoImage(file=".\\AED\\Exemplo - exame normal\\images\\refresh.png")
imgVerMais = PhotoImage(file=".\\AED\\Exemplo - exame normal\\images\\btn+.png")

btnAdicionar = Button(panel1, width=50, height=50, image=imgAdicionar, command=adicionarMusica)
btnAdicionar.place(x=10, y=100)

btnRefresh = Button(panel1, width=50, height=50, image=imgRefresh, command=mostrarMusicas)
btnRefresh.place(x=200, y=100)

# Painel mais informações
panel2 = PanedWindow(window, width=550, height=150, bd="3", relief="sunken")
panel2.place(x=20, y=300)

btnVerMais = Button(panel2, width=50, height=50, image=imgVerMais, command=verMaisInfo)
btnVerMais.place(x=10, y=20)

lb3 = Label(panel2, text="Nº de músicas", font=("Helvetica", "10"))
lb4 = Label(panel2, text="Música + vista", font=("Helvetica", "10"))
lb5 = Label(panel2, text="Link:", font=("Helvetica", "10"))
lb3.place(x=170, y=30)
lb4.place(x=170, y=70)
lb5.place(x=170, y=110)

txtNumFilmes = Entry(panel2, width=10)
txtMaisVisto = Entry(panel2, width=30)
txtLink = Entry(panel2, width=30)
txtNumFilmes.place(x=270, y=30)
txtMaisVisto.place(x=270, y=70)
txtLink.place(x=270, y=110)

canvas = Canvas(window, width=300, height=150, bd=4, relief="sunken")
canvas.place(x=630, y=300)

btnSelecionarImg = Button(window, width=18, height=2, text="Selecionar Imagem", command=selecionarImagem)
btnSelecionarImg.place(x=630, y=465)

# Inicializa a lista de bandas
lerBandas()

window.mainloop()
