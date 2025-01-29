# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import *
from PIL import Image

# ---------------INICIO DA INTERFACE GRAFICA ---------------------
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
app.configure(fg_color="#101010")  # Fundo da aplicação
app.iconbitmap(".\\Images\\1-f8c98aa8.ico")
renderWindow(1280, 832, "GameON!")

# ---------------PÁGINA PRINCIPAL---------------------
#-----------------------------------------------------------------
def homePage():
    for widget in app.winfo_children():
        widget.destroy()

    # Sidebar com botões
    sidebar = ctk.CTkFrame(app, width=300, height=832, corner_radius=0, fg_color="#1A1A1A")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    # Logo GameON
    imgIcon = ctk.CTkImage(Image.open(".\\Images\\Logo.png"), size=(180, 70))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#1A1A1A")
    imgIcon_label.pack(pady=(30, 20))

    # Botões da Sidebar
    buttons = ["LIBRARY", "STORE", "WISHLIST", "DISCOVER"]
    for btn in buttons:
        button = ctk.CTkButton(
            sidebar, text=btn, text_color="white", fg_color="#383838",
            font=("Arial", 12), hover_color="#5A5A5A", command=lambda btn=btn: print(f"{btn}"),
            width=220, height=40
        )
        button.pack(pady=10)

    # Botão Profile Settings
    profile_settingsBtn = ctk.CTkButton(
        sidebar, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
        font=("Arial", 12), hover_color="#FF4500", command=app, width=220, height=40
    )
    profile_settingsBtn.pack(side=ctk.BOTTOM, pady=30)

    # Topbar
    topbar = ctk.CTkFrame(app, height=100, corner_radius=0, fg_color="#1A1A1A")
    topbar.pack(side=ctk.TOP, fill=ctk.X)

    # Barra de busca
    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 14), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=(0, 30), pady=30)

    # Botão de perfil
    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25, fg_color="#FF5900",
                                   text="", hover_color="#FF4500")
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    # Título da seção atual
    section_label = ctk.CTkLabel(topbar, text="STORE", text_color="white", font=("Arial", 18, "bold"))
    section_label.pack(side=ctk.LEFT, padx=30)

    # Área principal
    main_area = ctk.CTkFrame(app, fg_color="#101010")
    main_area.pack(fill=ctk.BOTH, expand=True)

    # Sugestões
    suggest_frame = ctk.CTkFrame(main_area, fg_color="#FF5900", height=100, width=900, corner_radius=10)
    suggest_frame.pack(pady=(20, 10))

    suggest_label = ctk.CTkLabel(suggest_frame, text="SUGGEST GAMES", font=("Arial", 16, "bold"), text_color="black")
    suggest_label.place(relx=0.5, rely=0.5, anchor="center")

    # Jogos (Exemplo de 3 categorias)
    categories = ["ACTION", "ADVENTURE", "RPG"]
    for idx, category in enumerate(categories):
        category_label = ctk.CTkLabel(main_area, text=category, font=("Arial", 14, "bold"), text_color="white")
        category_label.pack(anchor="w", padx=50)

        games_frame = ctk.CTkFrame(main_area, fg_color="#101010")
        games_frame.pack(fill="x", padx=50, pady=10)

        for i in range(3):
            game_card = ctk.CTkFrame(games_frame, fg_color="#D9D9D9", width=200, height=250, corner_radius=10)
            game_card.pack(side=ctk.LEFT, padx=10)

            game_label = ctk.CTkLabel(game_card, text=f"GAME {i + 1}", font=("Arial", 12, "bold"), text_color="black")
            game_label.place(relx=0.5, rely=0.4, anchor="center")

            price_label = ctk.CTkLabel(game_card, text="Name game\nPrice", font=("Arial", 10), text_color="black")
            price_label.place(relx=0.5, rely=0.7, anchor="center")

            heart_icon = ctk.CTkLabel(game_card, text="\u2764", font=("Arial", 14), text_color="#FF5900")
            heart_icon.place(relx=0.9, rely=0.9, anchor="center")

homePage()
app.mainloop()
