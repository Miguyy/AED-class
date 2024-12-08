import customtkinter
from tkinter import PhotoImage

app = customtkinter.CTk()

app.geometry("325x670")
app.title("Simulador de IMC")
app.configure(fg_color="white") 

frame_inputText = customtkinter.CTkFrame(app, width=300, height=150, fg_color="gray")
frame_inputText.place(x=15, y=10)

labelPeso = customtkinter.CTkLabel(app, text="Peso:", fg_color="gray", text_color="white", font=("Helvetica", 14))
labelPeso.place(x=40, y=40)

entryPeso = customtkinter.CTkEntry(app, width=100, fg_color="white", border_color="gray", text_color="black")
entryPeso.place(x=180, y=40)

labelAltura = customtkinter.CTkLabel(app, text="Altura em cm:", fg_color="gray", text_color="white", font=("Helvetica", 14))
labelAltura.place(x=40, y=80)

entryAltura = customtkinter.CTkEntry(app, width=100, fg_color="white", border_color="gray", text_color="black")
entryAltura.place(x=180, y=80)

def calc_IMC():
    peso = float(entryPeso.get())
    altura = float(entryAltura.get()) / 100  
    IMC_resultado = peso / (altura ** 2)
    resultado_label.configure(text=f"{IMC_resultado:.2f}")
    
btnCalc = customtkinter.CTkButton(app, text="Calcular\nIMC", command=calc_IMC, width=300, height=50, text_color="white", fg_color="blue")
btnCalc.place(x=15, y=180)

btnSair = customtkinter.CTkButton(app, text="Sair", command=app.quit, width=300, height=50, text_color="white", fg_color="blue")
btnSair.place(x=15, y=240)

frame_inputText = customtkinter.CTkFrame(app, width=300, height=100, fg_color="gray")
frame_inputText.place(x=15, y=300)

IMC_label = customtkinter.CTkLabel(app, text="Índice de Massa Corporal ", fg_color="gray", text_color="aqua", font=("Helvetica", 14))
IMC_label.place(x=80, y=320)

resultado_label = customtkinter.CTkLabel(app, text="", fg_color="gray", text_color="aqua", font=("Helvetica", 14))
resultado_label.place(x=80, y=350)

img = PhotoImage(file="AED/RSF9/images/IMC.gif")
img_label = customtkinter.CTkLabel(app, image=img, text="")
img_label.place(x=20, y=450)

app.mainloop()
