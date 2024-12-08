import customtkinter
import os

caminho_arquivo = os.path.join("files", "texto.txt")

def guardar_texto():
    texto = txtNotas.get("1.0", "end").strip()  
    os.makedirs("files", exist_ok=True)  
    arquivo = open(caminho_arquivo, "w", encoding="utf-8")
    arquivo.write(texto)  
    arquivo.close()  

def limpar_texto():
    txtNotas.delete("1.0", "end")  

def ler_texto():
    if os.path.exists(caminho_arquivo):  
        arquivo = open(caminho_arquivo, "r", encoding="utf-8")  
        conteudo = arquivo.read() 
        arquivo.close() 
        txtNotas.delete("1.0", "end")  
        txtNotas.insert("1.0", conteudo) 
    else:
        txtNotas.delete("1.0", "end")
        txtNotas.insert("1.0", "O arquivo não foi encontrado.")  

app = customtkinter.CTk()
app.geometry("300x600")
app.title("My Notepad")
app.configure(fg_color="grey")

labelNotas = customtkinter.CTkLabel(app, text="Indique as suas notas", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
labelNotas.place(x=75, y=40)  

txtNotas = customtkinter.CTkTextbox(app, width=250, height=300, border_color="grey", fg_color="white", text_color="black")
txtNotas.place(x=25, y=80)  

btnGuardar = customtkinter.CTkButton(app, text="Guardar", command=guardar_texto, width=250, height=50, text_color="aqua", fg_color="black")
btnGuardar.place(x=25, y=400)  

btnLimpar = customtkinter.CTkButton(app, text="Limpar", command=limpar_texto, width=250, height=50, text_color="aqua", fg_color="black")
btnLimpar.place(x=25, y=460) 

btnLer = customtkinter.CTkButton(app, text="Ler Bloco de Notas", command=ler_texto, width=250, height=50, text_color="aqua", fg_color="black")
btnLer.place(x=25, y=520) 

app.mainloop()
