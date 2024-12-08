import customtkinter
from tkinter import PhotoImage

app = customtkinter.CTk()

app.geometry("370x430")
app.title("Simulador de Peso Ideal")
app.configure(fg_color="white") 

labelAltura_utilizador = customtkinter.CTkLabel(app, text="Altura em cm:", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
labelAltura_utilizador.place(x=40, y=40) 

entryAltura_utilizador = customtkinter.CTkEntry(app, width=150, fg_color="white", border_color="gray", text_color="black")
entryAltura_utilizador.place(x=180, y=40)

labelGen = customtkinter.CTkLabel(app, text="Género: ", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
labelGen.place(x=40, y=120)

radioVariable = customtkinter.StringVar(value="Masculino")  
radiobutton1 = customtkinter.CTkRadioButton(app, text="Masculino", variable=radioVariable, value="Masculino")
radiobutton1.place(x=180, y=140)
radiobutton2 = customtkinter.CTkRadioButton(app, text="Feminino", variable=radioVariable, value="Feminino")
radiobutton2.place(x=180, y=180)

def calcular_peso_ideal():
        altura = float(entryAltura_utilizador.get()) 
        match radioVariable.get():
            case "Masculino":
                k = 4
            case "Feminino":
                k = 2
            case _:
                k = None  
        peso_ideal = (altura - 100) - ((altura - 150) / k)
        resultado_label.configure(text=peso_ideal)

img = PhotoImage(file="AED\\RSF9\\images\\PesoIdeal.png")  

btnCalc = customtkinter.CTkButton(app, text="Calcular Peso Ideal", image=img, command=calcular_peso_ideal, width=370, height=80, text_color="aqua", fg_color="black")
btnCalc.place(x=0, y=220) 

peso_ideal_label = customtkinter.CTkLabel(app, text="Peso Ideal: ", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
peso_ideal_label.place(x=40, y=320)

resultado_label = customtkinter.CTkLabel(app, text="", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
resultado_label.place(x=40, y=350)

app.mainloop()
