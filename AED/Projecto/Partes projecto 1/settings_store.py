# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import tkinter as tk  
from tkinter import filedialog
from tkinter import ttk
import os
from PIL import Image, ImageDraw
import base64


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
    app.resizable(True, True)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap("Images/1-f8c98aa8.ico")
renderWindow(1180, 732, "GameON!")

# ---------------FRAMES ---------------------
#-----------------------------------------------------------------
def showFrame(frame):
    """
    Oculta todos os frames e exibe apenas o especificado.
    """
    for widget in app.winfo_children():
        widget.destroy()
    frame.pack(fill="both", expand=True)

# ---------------PARTES PÁGINA PRINCIPAL---------------------
#-----------------------------------------------------------------
def storePageUI():
    # --------------DESIGN PÁGINA STORE ---------------------
    #-----------------------------------------------------------------
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

    global profile_circle

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    store_label = ctk.CTkLabel(topbar, text="STORE", text_color="white", font=("Arial", 18))
    store_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    game_frame = ctk.CTkFrame(app, fg_color="#101010", width=800, height=400)
    game_frame.pack(pady=100)

    game1_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game1_button = ctk.CTkButton(game_frame, image=game1_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: gameAspect())
    game1_button.place(x=30, y=26)
    game1Txt = ctk.CTkLabel(game_frame, text="GAME 1", text_color="white", font=("Arial", 18))
    game1Txt.place(x=100, y=340)

    game2_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game2_button = ctk.CTkButton(game_frame, image=game2_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: gameAspect())
    game2_button.place(x=310, y=26)
    game2Txt = ctk.CTkLabel(game_frame, text="GAME 2", text_color="white", font=("Arial", 18))
    game2Txt.place(x=380, y=340)

    game3_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game3_button = ctk.CTkButton(game_frame, image=game3_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: gameAspect())
    game3_button.place(x=580, y=26)
    game3Txt = ctk.CTkLabel(game_frame, text="GAME 3", text_color="white", font=("Arial", 18))
    game3Txt.place(x=650, y=340)

def settingsPageUI():
    # --------------DESIGN PÁGINA SETTINGS ---------------------
    #-----------------------------------------------------------------
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

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    settings_label = ctk.CTkLabel(topbar, text="SETTINGS", text_color="white", font=("Arial", 18))
    settings_label.pack(side=ctk.LEFT, padx=35, pady=50)

    user_info_frame = ctk.CTkFrame(app, width=875, height=450, fg_color="black")
    user_info_frame.place(x=370, y=160) 

    global profile_circle
    profile_circle = ctk.CTkButton(user_info_frame, width=100, height=100, corner_radius=77, fg_color="#FFA500", text="", hover_color="#FF5900", command=lambda:selectProfileImage())
    profile_circle.place(x=5, y=5)

    username_label = ctk.CTkLabel(user_info_frame, text="USERNAME", text_color="white", font=("Arial", 40, "bold"))
    username_label.place(x=120, y=15)

    personal_info = ctk.CTkLabel(user_info_frame, text="EMAIL:", text_color="white", font=("Arial", 22), justify="left")
    personal_info.place(x=120, y=65)

    change_password_button = ctk.CTkButton(user_info_frame, text="CHANGE PASSWORD", text_color="white", fg_color="#383838", font=("Arial", 22), hover_color="#5A5A5A", width=140, height=33, command=" ")
    change_password_button.place(x=550, y=65)

    notifications_frame= ctk.CTkFrame (app, width=800, height=51, corner_radius=10, fg_color="#FFA500")
    notifications_frame.place(x=370, y=300)

    notifications_label = ctk.CTkLabel(notifications_frame, text="NOTIFICATIONS", text_color="black", font=("Arial", 22, "bold"))
    notifications_label.place(x=10, rely=0.5, anchor="w") 

    TxtObs = ctk.CTkTextbox(app, width=800, height=200, fg_color="white", text_color="black", font=("Arial", 14))
    TxtObs.place(x=370, y=360)

    msgSettings_frame= ctk.CTkFrame (app, width=600, height=52, corner_radius=10, fg_color="#FFA500")
    msgSettings_frame.place(x=370, y=580)

    msgSettings_label = ctk.CTkLabel(msgSettings_frame, text="YOU'RE A PRO PLAYER, DON'T GIVE UP", text_color="black", font=("Arial", 22, "bold"))
    msgSettings_label.place(relx=0.5, rely=0.5, anchor="center")

    logoutBtn = ctk.CTkButton(app, text="LOGOUT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=191, height=52, command=lambda:loginUI())
    logoutBtn.place(x=980, y=580)

    deleteAccountBtn= ctk.CTkButton(app, text="DELETE ACCOUNT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=800, height=55, command=lambda:deletePageUI())
    deleteAccountBtn.place(x=370, y=650)

app.mainloop()
