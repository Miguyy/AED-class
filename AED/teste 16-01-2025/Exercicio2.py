import customtkinter
import CTkMessagebox             # MessageBox
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk, Image    # Imagens .jpg ou .png
import os   
import datetime

# IDENTIFICAÇÃO DO ESTUDANTE    
# Numero : 40230260
# Ñome: Miguel Machado


# Funções solicitadas
#-----------------------------------------------------

def viewTrails(): #função para ver os trails
    tree.delete(*tree.get_children())   
    data = []

    if ck1_var.get(): #checkbox 1
        f = open("./ficheiros/trails.txt", "r") #ler ficheiro
        data += [line.strip().split(",") for line in f.readlines()]
        f.close()

    if ck2_var.get(): #checkbox 2
        f = open("./ficheiros/ultratrails.txt", "r") #ler ficheiro
        data += [line.strip().split(",") for line in f.readlines()]
        f.close()

    for row in data: #ler linha
        tree.insert("", "end", values=row)

    txtNumProvas.configure(state="normal")
    txtNumProvas.delete(0, "end")
    txtNumProvas.insert(0, str(len(data)))
    txtNumProvas.configure(state="readonly")

def ordAsc():   #função ordem ascendente
    data = sorted(tree.get_children(), key=lambda x: tree.item(x)["values"][0].lower())
    reorganize_tree(data)

def ordDesc(): #função ordem descendente
    data = sorted(tree.get_children(), key=lambda x: tree.item(x)["values"][0].lower(), reverse=True)
    reorganize_tree(data)

def reorganize_tree(data):
    items = [tree.item(i)["values"] for i in data]
    tree.delete(*tree.get_children())
    for item in items:
        tree.insert("", "end", values=item)

def notificacoes(): #função notificações
    provas = [
        (item["values"][1], item["values"][0]) 
        for item in (tree.item(i) for i in tree.get_children())
    ]
    provas.sort(key=lambda x: datetime.datetime.strptime(x[0], "%d-%m-%Y"))
    prova_proxima = provas[0] if provas else None

    if prova_proxima: #mensagens 
        CTkMessagebox.CTkMessagebox(title="Notificação", message= f"Prova mais próxima: {prova_proxima[1]} em {prova_proxima[0]}", icon="info", option_1="Ok")
    else:
        CTkMessagebox.CTkMessagebox(title="Notificação", message="Nenhuma prova disponível.", icon="info", option_1="Ok")

def selecionarImagem(): #selecionar imagem
    file_path = filedialog.askopenfilename(initialdir="./imagens", title="Selecionar Imagem",
                                           filetypes=(("Imagens PNG", "*.png"), ("Imagens JPG", "*.jpg")))
    if file_path:
        img = customtkinter.CTkImage(Image.open(file_path), size=(180, 180))
        btnImagem.configure(image=img)

def addFavoritos(): #favoritos
    selected = tree.selection()
    if selected:
        prova = tree.item(selected[0])["values"]
        lboxFav.insert("end", ", ".join(prova))
    else:
        CTkMessagebox.CTkMessagebox(title="Atenção", message="Selecione uma prova antes de adicionar aos favoritos.", icon="warning", option_1="Ok")

def fileFavoritos():
    favoritos = lboxFav.get("1.0", "end").strip()
    if favoritos:
        os.makedirs("ficheiros", exist_ok=True)
        f = open("ficheiros/favoritos.txt", "w")
        f.write(favoritos)
        f.close()
        CTkMessagebox.CTkMessagebox(title="Sucesso", message="Favoritos guardados em ficheiros/favoritos.txt")
    else:
        CTkMessagebox.CTkMessagebox(title="Atenção", message="Nenhum favorito para guardar.")

#----------------------------------------------------
# GUI  INTERFACE GRÁFICA -----------------------------------------------
#----------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões
    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

#parte visual
app = customtkinter.CTk() 
renderWindow(1000, 500, "Trails App")

ck1_var = customtkinter.BooleanVar(value=False)
ck2_var = customtkinter.BooleanVar(value=True)

ck1 = customtkinter.CTkCheckBox(app, text="Trail Curto", variable=ck1_var)
ck2 = customtkinter.CTkCheckBox(app, text="Ultra Trail", variable=ck2_var)
ck1.place(x=50, y=20)
ck2.place(x=150, y=20)



tree = ttk.Treeview(app, columns=("Prova", "Data", "Local", "Km"), show="headings", height=12, selectmode="browse")
tree.column("Prova", width=220, anchor="w")
tree.column("Data", width=100, anchor="c")
tree.column("Local", width=200, anchor="c")
tree.column("Km", width=120, anchor="c")
tree.heading("Prova", text="Prova")
tree.heading("Data", text="Data")
tree.heading("Local", text="Local")
tree.heading("Km", text="Km")
tree.place(x=20, y=100)

lblNumProvas = customtkinter.CTkLabel(app, text="Nº de provas", font=("Helvetica", 13))
lblNumProvas.place(x=50, y=320)

txtNumProvas = customtkinter.CTkEntry(app, width=50, state="readonly")
txtNumProvas.place(x=150, y=320)

btnSelecionarImg = customtkinter.CTkButton(app, width=45, height=45, text="Selecionar Imagem", fg_color="black",
                                           text_color="cyan", command=selecionarImagem)#função
btnSelecionarImg.place(x=180, y=430)

img = customtkinter.CTkImage(Image.open("./imagens/img1.png"), size=(180, 180))
btnImagem = customtkinter.CTkButton(app, width=180, height=180, image=img, text="", fg_color="transparent")
btnImagem.place(x=330, y=300)

btnAddFav = customtkinter.CTkButton(app, text="Adicionar >>\n Favoritos", height=45, fg_color="black",
                                    text_color="cyan", command=addFavoritos) #função
btnAddFav.place(x=550, y=150)

frame1 = customtkinter.CTkFrame(app, width=300, height=500)
frame1.place(x=700, y=1)

lblFav = customtkinter.CTkLabel(frame1, text="Favoritos", font=("Helvetica", 14))
lblFav.place(x=100, y=30)

lboxFav = customtkinter.CTkTextbox(frame1, width=250, height=250, fg_color="gray", text_color="white")
lboxFav.place(x=20, y=60)

btnImageGuardar = customtkinter.CTkImage(Image.open("./imagens/GuardarFile.png"), size=(35, 35))
btnGuardarFav = customtkinter.CTkButton(frame1, text="Guardar Favoritos", image=btnImageGuardar, height=90, width=250, fg_color="black",
                                        text_color="cyan", command=fileFavoritos)#função
btnGuardarFav.place(x=20, y=320)

app.mainloop()
