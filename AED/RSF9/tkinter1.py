import customtkinter

app = customtkinter.CTk()

app.geometry("600x300")
app.title("Países do Mundo!")
app.configure(fg_color="white") 

labelPais = customtkinter.CTkLabel(app, text="País", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
labelPais.place(x=15, y=40)
labelContinente = customtkinter.CTkLabel(app, text="Continente", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
labelContinente.place(x=15, y=80)

strPais=customtkinter.StringVar()
strPais.set("Portugal")

entryPais = customtkinter.CTkEntry(app, width=150, fg_color="white", textvariable=strPais)  
entryPais.place(x=100, y=40)
entryContinente = customtkinter.CTkEntry(app, width=150, fg_color="white")  
entryContinente.place(x=100, y=80)

listaContinentes = ["África", "Ásia", "América", "Europa", "Oceania"]

combContinente = customtkinter.CTkComboBox(app, values=listaContinentes, width=150, fg_color="white") 
combContinente.place(x=100, y=80)


labelHemisferio = customtkinter.CTkLabel(app, text="Hemisfério", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
labelHemisferio.place(x=15, y=120)


radioVariable = customtkinter.StringVar(value="Norte")  
radiobutton1 = customtkinter.CTkRadioButton(app, text="Norte", variable=radioVariable, value="Norte")
radiobutton1.place(x=100, y=140)
radiobutton2 = customtkinter.CTkRadioButton(app, text="Sul", variable=radioVariable, value="Sul")
radiobutton2.place(x=100, y=180)

labelIdioma = customtkinter.CTkLabel(app, text="Idioma Oficial", fg_color="transparent", text_color="blue", font=("Helvetica", 14))
labelIdioma.place(x=350, y=40)

checkVarPT = customtkinter.StringVar(value="on")  
checkVarEN = customtkinter.StringVar(value="off")
checkVarFR = customtkinter.StringVar(value="off")
checkVarOT = customtkinter.StringVar(value="off")

checkboxPT = customtkinter.CTkCheckBox(app, text="Português", variable=checkVarPT, onvalue="on", offvalue="off")
checkboxPT.place(x=300, y=80)
checkboxEN = customtkinter.CTkCheckBox(app, text="Inglês", variable=checkVarEN, onvalue="on", offvalue="off")
checkboxEN.place(x=400, y=80)
checkboxFR = customtkinter.CTkCheckBox(app, text="Francês", variable=checkVarFR, onvalue="on", offvalue="off")
checkboxFR.place(x=300, y=120)
checkboxOT = customtkinter.CTkCheckBox(app, text="Outro", variable=checkVarOT, onvalue="on", offvalue="off")
checkboxOT.place(x=400, y=120)

btnGuardar=customtkinter.CTkButton(app,text="Guardar", command="", width=100, height=40, fg_color="grey")
btnGuardar.place(x=400,y=250)
btnLimpar=customtkinter.CTkButton(app,text="Limpar", command=" ", width=100, height=40, fg_color="grey",state="disabled")
btnLimpar.place(x=500,y=250)

app.mainloop()
