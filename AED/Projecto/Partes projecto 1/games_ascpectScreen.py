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

# ---------------ASPECTO JOGOS---------------------
#-----------------------------------------------------------------
def gameAspect():
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
    
    game_label = ctk.CTkLabel(topbar, text="GAME NAME", text_color="white", font=("Arial", 18))
    game_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    imgGame = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    imgGame_label = ctk.CTkLabel(app, image=imgGame, text="", fg_color="#2E2B2B")
    imgGame_label.place(x=350, y=200)

    nameGame_label = ctk.CTkLabel(app, text="GAME NAME", text_color="white", font=("Arial", 18))
    nameGame_label.place(x=580, y=220)

    gameDescription=ctk.CTkTextbox(app, width=480, height=180, fg_color="white", font=("Arial", 12), text_color="black")
    gameDescription.place(x=350, y=520)

    saveBtn = ctk.CTkButton(app, text="SAVE", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37,
                            border_color="black", text_color="black",font=ctk.CTkFont(size=20, weight="bold"), command="")
    saveBtn.place(x=580, y=260) 

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900",
                            width=292, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:storePageUI())
    backBtn.place(x=350, y=150)

    comment_frame=ctk.CTkFrame(app, fg_color="#101010", width=300, height=520, corner_radius=10)
    comment_frame.place(x=860, y=150)

    commentZone=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone.place(x=10, y=20)

    commentZone2=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone2.place(x=10, y=150)

    commentZone3=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone3.place(x=10, y=280)

    commentZone3=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone3.place(x=10, y=410)

    createCommentBtn = ctk.CTkButton(app, text="CRATE A COMMENT", fg_color="#FFA500", hover_color="#FF5900",
                            width=300, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:commentsPage())
    createCommentBtn.place(x=860, y=680)

gameAspect()
app.mainloop()
