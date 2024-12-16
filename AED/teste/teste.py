# Biblioteca Tkinter: UI
import customtkinter
import CTkMessagebox
from PIL import Image
from tkinter import ttk          # treeview
import os

mesesFile = ".\\Atividade de Progresso 4\\files\\meses.txt"
def lerFicheiro(ficheiro):
    """
    Lê um ficheiro determinado previamente
    """
    lista = []
    if os.path.exists(ficheiro):   # Ficheiro existe
        file = open(ficheiro, "r", encoding="utf-8") 
        lista = file.readlines()
        file.close()    
    return lista

def consultarTree(tree,mes,filter,label1,label2):
    """
    Atualiza a tree view para consulta com os filtros selecionados e atualiza as labels numero e valor
    Arg:tree, mes selcionado e filtros selecionados
    """
    mes=mes.replace("\n","")#formatar o mes
    despesasN=0#despesa numero
    despesasV=0#despesa valor
    if mes=="":#mensagem sem mes
        CTkMessagebox.CTkMessagebox(title="DespesasApp", message="Não selecionou mes",
                        icon="warning", option_1="Ok")
    tree.delete(*tree.get_children()) #reinicia a tree
    lista = lerFicheiro(".\\Atividade de Progresso 4\\files\\"+mes+".txt")
    if lista==[]:#mensagem sem despesas
        CTkMessagebox.CTkMessagebox(title="DespesasApp", message="Não existem despesas para este mes",
                icon="cancel", option_1="Ok")
    for linha in lista:#adiciona as linhas a tree
        campos = linha.split(";")
        if filter.get()+"\n"==campos[2] or filter.get()=="Todas":#filtra segundo os butoes selecionados
            tree.insert("", "end", values = (campos[0], campos[1], campos[2]))
            despesasN+=1
            despesasV+=int(campos[1])
    #Atualiza a label Numero
    label1.destroy()
    label1 =customtkinter.CTkLabel(app, text = despesasN)
    label1.place(x=150, y=520)
    #Atualiza a label Valor
    label2.destroy()#tentativa de correção
    label2 =customtkinter.CTkLabel(app, text = despesasV )
    label2.place(x=350, y=520)#erro no display labels antigas continuam a aparecer



# ---------------INICIO DA INTERFACE GRAFICA  ---------------------
#-----------------------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False) 




app = customtkinter.CTk()
renderWindow(450, 550, "DespesasApp")

#--- FRAME 1 - frame com os critérios de consulta ------------------------
frame1 = customtkinter.CTkFrame(app, width=430, height=170, fg_color="gray")
frame1.place(x=10, y=10)

labelMes = customtkinter.CTkLabel(frame1, text = "Mês de Consulta de Despesas: ")
labelMes.place(x=20, y= 10)


mes = customtkinter.StringVar()
# Combobox que deverá conter os meses de Janeiro a Dezembro, a partir da leitura do ficheiro meses.txt
listaMes = lerFicheiro(mesesFile)
comboboxMes = customtkinter.CTkComboBox(frame1,values=listaMes, height= 12, variable=mes)
comboboxMes.place(x=250, y=10)

rbState = customtkinter.StringVar(value="Todas")#Valor Todas como default

rb1 = customtkinter.CTkRadioButton(frame1, text = "Dinheiro",   variable = rbState, value = "Dinheiro")
rb2 = customtkinter.CTkRadioButton(frame1, text = "Credito",    variable = rbState, value = "Credito")
rb3 = customtkinter.CTkRadioButton(frame1, text = "Todas",      variable = rbState, value = "Todas")
rb1.place (x=20, y=60)
rb2.place (x=20, y=90)
rb3.place (x=20, y=120)


imageIco = customtkinter.CTkImage(Image.open(".\\Atividade de Progresso 4\\images\\lupa.png"), size=(64, 64))
btnConsultar = customtkinter.CTkButton(frame1, width=150, height=70, text="Consultar", text_color="cyan", image=imageIco, compound="right",
                                        command=lambda: consultarTree(tree, mes.get(), rbState,lblNumDespesas,lblValorTotal))
btnConsultar.place(x=235, y=70)

#----------------FRAME COM A TREEVIEW ----------------------------------
#-----------------------------------------------------------------------
frame2 = customtkinter.CTkFrame(app, width=430, height=320)
frame2.place(x=10, y=200)

tree = ttk.Treeview(frame2, columns = ("Descrição", "Valor", "Estado"), show = "headings", height = 17)
tree.column("Descrição", width = 240, anchor = "w")
tree.column("Valor", width = 130, anchor = "c")
tree.column("Estado", width = 130, anchor = "c")
tree.heading("Descrição", text = "Descrição")
tree.heading("Valor", text = "Valor")
tree.heading("Estado", text = "Estado")
tree.place(x=17, y=15)


#----------------Nº de Despesas e Valor, na base da janela da app
#------------------------------------------------------------------
lblDespesas = customtkinter.CTkLabel(app, text = "Nº de Despesas:" )
lblTotal = customtkinter.CTkLabel(app, text = "Valor Total: ")
lblDespesas.place (x= 50, y=520)
lblTotal.place (x= 250, y=520)

#----- LABEL do Número de Despesas
lblNumDespesas =customtkinter.CTkLabel(app, text = "")
lblNumDespesas.place(x=150, y=520)

# - LABEL do Valor Total de Despesas
lblValorTotal =customtkinter.CTkLabel(app, text = "" )
lblValorTotal.place(x=350, y=520)




app.mainloop()   # event listening loop by calling the mainloop()