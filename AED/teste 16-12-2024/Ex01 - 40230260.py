#40230260
#Miguel Machado
# biblioteca Tkinter: UI
import customtkinter
import CTkMessagebox
from PIL import Image
from tkinter import ttk          # importação da biblioteca tkinter
import os

mesesFile = ".\\files\\meses.txt"
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
    Actualização da treeview para as formatações solicitadas
    """
    mes=mes.replace("\n","") #formatação do "mês"
    despesasN=0 #nº despesa
    despesasV=0 #valor despesa
    if mes=="": #mensagem vazia / sem mês
        CTkMessagebox.CTkMessagebox(title="DespesasApp", message="Não seleccionou um mês!",
                        icon="warning", option_1="Ok") #messagebox com o ícone "Warning" e apenas com a opção "Ok"
    tree.delete(*tree.get_children()) #reinicia a treeview
    lista = lerFicheiro(".\\files\\"+mes+".txt") #leitura do ficheiro txt, utilizando a funcção criada de leitura 
    if lista==[]:   #criacção de uma lista vazia, que se refere a "não" haver despesas
        CTkMessagebox.CTkMessagebox(title="DespesasApp", message="Não existem despesas para este mes!",
                icon="cancel", option_1="Ok") #messagebox com o ícone "Cancel" e apenas com a opção "Ok"
    for linha in lista: #metologia utilizada nos exercício realizados nas aulas sobre ficheiros
        campos = linha.split(";") #divisão dos campos por ";"
        if filter.get()+"\n"==campos[2] or filter.get()=="Todas": #filtragem a partir dos botões seleccionados
            tree.insert("", "end", values = (campos[0], campos[1], campos[2])) #utilização de campos que permitem identificar a localização, para onde deverá ir a informação
            despesasN+=1
            despesasV+=int(campos[1])
    #actualiza a label número
    label1.destroy()
    label1 =customtkinter.CTkLabel(app, text = despesasN)
    label1.place(x=150, y=520)
    #actualiza a label valor
    label2.destroy() 
    label2 =customtkinter.CTkLabel(app, text = despesasV )
    label2.place(x=350, y=520)  



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
# combobox que deverá conter os meses de Janeiro a Dezembro, a partir da leitura do ficheiro meses.txt
listaMes = lerFicheiro(mesesFile)
comboboxMes = customtkinter.CTkComboBox(frame1,values=listaMes, height= 12, variable=mes)
comboboxMes.place(x=250, y=10)

rb_estado = customtkinter.StringVar(value="Todas") #radio button "Todas", foi inicializada como padrão
#para ser intrepertado, foi colocada a variável rb_estado, para assim ser possível saber que vai ser inicializado com o "Todas"
rb1 = customtkinter.CTkRadioButton(frame1, text = "Dinheiro",   variable = rb_estado, value = "Dinheiro")
rb2 = customtkinter.CTkRadioButton(frame1, text = "Crédito",    variable = rb_estado, value = "Credito")
rb3 = customtkinter.CTkRadioButton(frame1, text = "Todas",      variable = rb_estado, value = "Todas")
rb1.place (x=20, y=60)
rb2.place (x=20, y=90)
rb3.place (x=20, y=120)


imgConsultar = customtkinter.CTkImage(Image.open(".\\images\\lupa.png"), size=(64, 64)) #implementação do ícone da lupa
btnConsultar = customtkinter.CTkButton(frame1, width=150, height=70, text="Consultar", text_color="cyan", image=imgConsultar, compound="right",
                                        command=lambda: consultarTree(tree, mes.get(), rb_estado,lblNumDespesas,lblValorTotal)) #este botão apresenta, agora, uma função que permite que o mesmo funcione
btnConsultar.place(x=235, y=70)

#----------------FRAME COM A TREEVIEW ----------------------------------
#-----------------------------------------------------------------------
frame2 = customtkinter.CTkFrame(app, width=430, height=320)
frame2.place(x=10, y=200)

tree = ttk.Treeview(frame2, columns = ("Descrição", "Valor", "Estado"), show = "headings", height = 17)
tree.column("Descrição", width = 240, anchor = "w")
tree.column("Valor", width = 130, anchor = "c")         #c - center
tree.column("Estado", width = 130, anchor = "c")        #w - west
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
lblNumDespesas =customtkinter.CTkLabel(app, text = "") #vai escrever o número
lblNumDespesas.place(x=150, y=520)

# - LABEL do Valor Total de Despesas
lblValorTotal =customtkinter.CTkLabel(app, text = "" ) #vai escrever o valor
lblValorTotal.place(x=350, y=520)

app.mainloop()   #fim do loop e chamar o mesmo