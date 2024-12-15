import customtkinter
from PIL import Image
import CTkMessagebox
from tkinter import ttk
import os

ficheiro = ".//files//presencas.txt"

app = customtkinter.CTk()

app.geometry("450x700")
app.title("Demo com containers")
app.configure(fg_color="white") 
app.resizable(False,False)

def lerFicheiro():
    fileTemp = open(ficheiro,"r")
    listaFile = fileTemp.readlines()
    fileTemp.close
    return listaFile

def mostrarDados():
    tree.delete(*tree.get_children())
    lista = lerFicheiro()
    for linha in lista:
        campos = linha.split(";")
        tree.insert("","end", values = (campos[0],campos[1],campos[2]))

def sair_app():
    msg=CTkMessagebox.CTkMessagebox(app, width=200, height=200, title="Sair da aplicação", message="Deseja sair da aplicação?", icon="question", option_1="Não", option_2="Sim")
    resposta=msg.get()
    if resposta=="Sim":
        app.destroy()
    else:
        print("A voltar para o menu principal.")

def admin_view():
    if True:  
        tab3 = tabview.add("Administrador")
        tab3 = tabview.set("Administrador")

tabview=customtkinter.CTkTabview(app,width=400, height=400, fg_color="black")
tabview.pack(padx=20,pady=20)

tab1=tabview.add("Gestor de Presenças")
tab2=tabview.add("Consultar")

img = customtkinter.CTkImage(Image.open(".//AED//RSF9//images//presencas.png"), size=(300, 280))
img_label = customtkinter.CTkLabel(tab1, image=img, text="", width=300, height=280)
img_label.place(x=45, y=2)

btnSair = customtkinter.CTkButton(app, text="Sair Aplicação", command=sair_app, width=300, height=30, text_color="white", fg_color="deepskyblue", bg_color="black")
btnSair.place(x=75, y=350)

btnAdmin = customtkinter.CTkButton(app, text="Ver Painel Admin", command=admin_view, width=300, height=30, text_color="white", fg_color="deepskyblue",bg_color="black")
btnAdmin.place(x=75, y=385)

tab_consultar = tabview.tab("Consultar")

btnDados = customtkinter.CTkButton(tab_consultar, text="Consultar dados", command=mostrarDados, width=300, height=30, fg_color="deepskyblue", text_color="white",bg_color="black")
btnDados.pack(pady=10)

tree = ttk. Treeview(tab2, height = 15, selectmode = "browse",columns = ("Data", "Hora", "Temperatura"),show = "headings")
tree.column("Data", width = 140,anchor="c")
tree.column("Hora", width = 140,anchor="c")
tree.column("Temperatura", width = 140, anchor="c")
tree.heading("Data", text = "Data")
tree.heading("Hora", text = "Hora")
tree.heading("Temperatura", text = "Temperatura")
tree.place(x= 40, y=60)

app.mainloop()