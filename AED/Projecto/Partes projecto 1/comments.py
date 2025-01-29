# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
from PIL import Image

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
    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap(".\\Images\\1-f8c98aa8.ico")
renderWindow(1180, 732, "GameON!")

# ---------------PÁGINA COMENTÁRIOS---------------------
#-----------------------------------------------------------------
def commentsPage():
    for widget in app.winfo_children():
        widget.destroy()

    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    commentsZone_label = ctk.CTkLabel(topbar, text="COMMENTS ZONE", text_color="white", font=("Arial", 18))
    commentsZone_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    ratingList = ["Select..." ,"1", "2", "3", "4", "5"]

    rating_label= ctk.CTkLabel(app, text="Rating", text_color="white", font=("Arial", 18))
    rating_label.place(x=540, y=200)

    rating=ctk.CTkComboBox(app, width=300, height=37, fg_color="white", values= ratingList, font=("Arial", 12), text_color="black", state="readonly")
    rating.place(x=640, y=200)
    rating.set("Select...")

    commentTxt=ctk.CTkTextbox(app, width=500, height=300, fg_color="white", font=("Arial", 12), text_color="black")
    commentTxt.place(x=480, y=260)

    commentBtn = ctk.CTkButton(app, text="COMMENT HERE", fg_color="#FFA500", hover_color="#FF5900",
                            width=292, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:"")
    commentBtn.place(x=580, y=600)

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900",
                            width=292, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:storePageUI())
    backBtn.place(x=580, y=650)

commentsPage()
app.mainloop()
