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

# ---------------LIBRARY---------------------
#-----------------------------------------------------------------
def libraryPage():
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open(".\\Images\\Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["LIBRARY", "STORE", "WISHLIST", "DISCOVER"]
    for btn in buttons:
        button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                            font=("Arial", 12), hover_color="#5A5A5A", command=lambda btn=btn: print(f"{btn}"),
                            width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=app, width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    discover_label = ctk.CTkLabel(topbar, text="MY LIBRARY", text_color="white", font=("Arial", 18))
    discover_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900")
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    game_frame = ctk.CTkFrame(app, fg_color="#101010", width=800, height=400)
    game_frame.pack(pady=40)

    game1_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game1_button = ctk.CTkButton(game_frame, image=game1_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: )
    game1_button.place(x=30, y=26)
    game1Txt = ctk.CTkLabel(game_frame, text="GAME 1", text_color="white", font=("Arial", 18))
    game1Txt.place(x=100, y=340)

    game2_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game2_button = ctk.CTkButton(game_frame, image=game2_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: )
    game2_button.place(x=310, y=26)
    game2Txt = ctk.CTkLabel(game_frame, text="GAME 2", text_color="white", font=("Arial", 18))
    game2Txt.place(x=380, y=340)

    game3_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game3_button = ctk.CTkButton(game_frame, image=game3_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: )
    game3_button.place(x=580, y=26)
    game3Txt = ctk.CTkLabel(game_frame, text="GAME 3", text_color="white", font=("Arial", 18))
    game3Txt.place(x=650, y=340)
libraryPage()
app.mainloop()
