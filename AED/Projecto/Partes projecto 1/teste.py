# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import tkinter as tk  
import os
import base64
from PIL import Image

# ---------------CRIAÇÃO DA PASTA USERS E CODIFICAÇÃO DA INFORMAÇÃO ---------------------
#-----------------------------------------------------------------
if not os.path.exists("users"):
    os.makedirs("users")

def encodeBinary(data):
    return base64.b64encode(data.encode()).decode()

def decodeBinary(data):
    return base64.b64decode(data.encode()).decode()

# ---------------VARIAVEIS GLOBAIS---------------------
#-----------------------------------------------------------------
currentUser = ""

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

# ---------------PARTES LOGIN---------------------
#-----------------------------------------------------------------
def loginFunction(username_entry,password_entry):
    # --------------FUNCIONALIDES LOGIN ---------------------
    #-----------------------------------------------------------------
    global currentUser
    login_input = username_entry.get().strip()  
    password = password_entry.get().strip() 

    if login_input and password:
        if '@' in login_input:
            userFound = False
            for file_name in os.listdir("users"):
                if file_name.endswith(".txt"):
                    userFile = os.path.join("users", file_name)
                    file = open(userFile, "r")
                    savedUsername = decodeBinary(file.readline().strip())
                    savedPassword = decodeBinary(file.readline().strip())
                    savedEmail = decodeBinary(file.readline().strip())
                    file.close()
                    if savedEmail == login_input: 
                        if savedPassword == password:  
                            currentUser = savedUsername
                            userFound = True
                            welcomeUI()
                        else:
                            messagebox.showerror("Error", "Wrong password.")
                            userFound = True
                        break
            if not userFound:
                messagebox.showerror("Error", "Email not found.")
        else:
            userFile = os.path.join("users", f"{login_input}.txt")
            if os.path.exists(userFile):
                file = open(userFile, "r")
                savedPassword = decodeBinary(file.readline().strip())
                file.close()
                if savedPassword == password:  
                    currentUser = login_input
                else:
                    messagebox.showerror("Error", "Wrong password.")
            else:
                messagebox.showerror("Error", "User not found.")
    else:
        messagebox.showwarning("Warning", "Fill all the fields.")
        
def loginUI():
    # --------------DESIGN LOGIN ---------------------
    #-----------------------------------------------------------------
    login_frame = ctk.CTkFrame(app, width=800, height=500, fg_color="#2E2B2B", corner_radius=15)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
    imgIcon_label = ctk.CTkLabel(login_frame, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(relx=0.5, rely=0.2, anchor="center")

    input_frame = ctk.CTkFrame(login_frame, width=550, height=350, fg_color="#2E2B2B")
    input_frame.place(relx=0.5, rely=0.6, anchor="center")  

    username_entry = ctk.CTkEntry(input_frame, fg_color="white", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="USERNAME / EMAIL", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    username_entry.pack(pady=5, anchor="center")

    password_entry = ctk.CTkEntry(input_frame, fg_color="white", show="*", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="PASSWORD", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    password_entry.pack(pady=5, anchor="center")

    button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    button_frame.pack(pady=(20, 20), anchor="center")

    loginBtn = ctk.CTkButton(button_frame, text="LOGIN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:loginFunction(username_entry,password_entry))
    loginBtn.pack(side="left", padx=5, anchor="center")

    signinBtn = ctk.CTkButton(button_frame, text="SIGN IN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:signinUI())
    signinBtn.pack(side="left", padx=5, anchor="center")

    qrcode_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    qrcode_frame.pack(pady=(5, 20), anchor="center")

    qrcodeBtn = ctk.CTkButton(qrcode_frame, text="QR CODE", fg_color="#FFA500", hover_color="#FF5900", 
                                width=292, height=37, border_color="#2E2B2B", text_color="black", 
                                font=ctk.CTkFont(size=20, weight="bold"), command=lambda:qrcodeFunction())
    qrcodeBtn.pack(padx=5, anchor="center")
    
# ---------------PARTES SIGN IN---------------------
#-----------------------------------------------------------------
def signinFunction(newUsernameEntry,newEmailEntry,newPasswordEntry):
    # --------------FUNCIONALIDES SIGN IN ---------------------
    #-----------------------------------------------------------------
    newUsername = newUsernameEntry.get().strip()
    newEmail = newEmailEntry.get().strip()
    newPassword = newPasswordEntry.get().strip()
    
    if newUsername and newEmail and newPassword:
        if '@' not in newEmail:
            messagebox.showwarning("Warning", "Please enter a valid email address with '@'.")
            return
        userFile = os.path.join("users", f"{newUsername}.txt")
        if not os.path.exists(userFile):
            file = open(userFile, "w")
            file.write(f"{encodeBinary(newUsername)}\n {encodeBinary(newPassword)}\n {encodeBinary(newEmail)}")
            file.close()
            messagebox.showinfo("Success", "Your account was created.")
            loginUI()
        else:
            messagebox.showwarning("Warning", "You already have an account.")
            loginUI()
    else:
        messagebox.showwarning("Warning", "Fill all the fields.")

def signinUI():
    # --------------DESIGN SIGN IN ---------------------
    #-----------------------------------------------------------------
    signin_frame = ctk.CTkFrame(app, width=800, height=500, fg_color="#2E2B2B", corner_radius=15)
    signin_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
    imgIcon_label = ctk.CTkLabel(signin_frame, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(relx=0.5, rely=0.2, anchor="center")

    input_frame = ctk.CTkFrame(signin_frame, width=550, height=350, fg_color="#2E2B2B")
    input_frame.place(relx=0.5, rely=0.6, anchor="center")  

    username_entry = ctk.CTkEntry(input_frame, fg_color="white", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="USERNAME", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    username_entry.pack(pady=5, anchor="center")

    email_entry = ctk.CTkEntry(input_frame, fg_color="white", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="EMAIL", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    email_entry.pack(pady=5, anchor="center")

    password_entry = ctk.CTkEntry(input_frame, fg_color="white", show="*", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="PASSWORD", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    password_entry.pack(pady=5, anchor="center")

    button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    button_frame.pack(pady=(20, 20), anchor="center")

    signinBtn = ctk.CTkButton(button_frame, text="SIGN IN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: signinFunction(username_entry, email_entry, password_entry))
    signinBtn.pack(side="left", padx=5, anchor="center")

    backBtn = ctk.CTkButton(button_frame, text="BACK", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:loginUI())
    backBtn.pack(side="left", padx=5, anchor="center")

# ---------------PARTES QR CODE---------------------
#-----------------------------------------------------------------
def qrcodeFunction():
    # --------------FUNCIONALIDADES E DESIGN QR CODE ---------------------
    #-----------------------------------------------------------------
    qrcode_frame = ctk.CTkFrame(app, width=800, height=500, fg_color="#2E2B2B", corner_radius=15)
    qrcode_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
    imgIcon_label = ctk.CTkLabel(qrcode_frame, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(relx=0.5, rely=0.2, anchor="center")

    input_frame = ctk.CTkFrame(qrcode_frame, width=550, height=350, fg_color="#2E2B2B")
    input_frame.place(relx=0.5, rely=0.9, anchor="center")  

    msg_qrcode_label = ctk.CTkLabel(qrcode_frame, text="SCAN & GO!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_qrcode_label.place(relx=0.5, rely=0.3, anchor="center")

    imgQR = ctk.CTkImage(Image.open("Images/frame.png"), size=(239, 239))
    imgQR_label = ctk.CTkLabel(qrcode_frame, image=imgQR, text="", fg_color="#2E2B2B")
    imgQR_label.place(relx=0.5, rely=0.6, anchor="center") 

    button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    button_frame.pack(pady=(20, 20), anchor="center")

    backBtn = ctk.CTkButton(button_frame, text="BACK", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:loginUI())
    backBtn.pack(side="left", padx=5, anchor="center")

# ---------------PARTES BEM VINDO---------------------
#-----------------------------------------------------------------
def draw_loading_circle(canvas, angle):
    # ---------------CANVAS PARA O LOADING ---------------------
    #-----------------------------------------------------------------
    canvas.delete("all")  
    canvas.create_oval(10, 10, 102, 102, width=10, outline="gray") 
    canvas.create_arc(10, 10, 102, 102, start=angle, extent=270, width=10, outline="orange") 

def update_loading_circle(canvas, angle):
    # ---------------CANVAS PARA O LOADING ---------------------
    #-----------------------------------------------------------------
    angle += 10  
    if angle >= 360:
        angle = 0  
    draw_loading_circle(canvas, angle)
    canvas.after(50, update_loading_circle, canvas, angle) 

def welcomeUI():
    # --------------DESIGN BEM VINDO ---------------------
    #-----------------------------------------------------------------
    
    welcome_frame = ctk.CTkFrame(app, width=1180, height=732, fg_color="black")
    welcome_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(450, 150))
    imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="")
    imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

    msg_welcome_label = ctk.CTkLabel(app, text="WELCOME!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_welcome_label.place(relx=0.5, rely=0.50, anchor="center")

    loading_canvas = tk.Canvas(app, width=120, height=120, bg="black", bd=0, highlightthickness=0)
    loading_canvas.place(relx=0.5, rely=0.65, anchor="center")

    update_loading_circle(loading_canvas, 0)

    msg_loading_label = ctk.CTkLabel(app, text="LOADING...", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_loading_label.place(relx=0.5, rely=0.80, anchor="center")

    app.after(5000, storePageUI)

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
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:" ",
                                width=247, height=44)
        button.pack(pady=5, padx=42)

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

    suggest_frame = ctk.CTkFrame(app, fg_color="#FFA500", height=190, width=674, corner_radius=100)
    suggest_frame.pack(pady=(20, 10))

    suggestBtn = ctk.CTkButton(suggest_frame, text="SUGGEST GAMES", text_color="black", fg_color="#FFA500",
                                        font=("Arial", 22, "bold"), hover_color="#FF5900", command=app, width=874, height=190)
    suggestBtn.place(relx=0.5, rely=0.5, anchor="center")

    categories = ["ACTION", "ADVENTURE", "RPG"]
    for idx, category in enumerate(categories):
        category_label = ctk.CTkLabel(app, text=category, font=("Arial", 14, "bold"), text_color="white")
        category_label.pack(anchor="w", padx=20)
    
        games_frame = ctk.CTkFrame(app, fg_color="#101010")
        games_frame.pack(fill="x", padx=20, pady=10)

        for i in range(3):
            game_card = ctk.CTkFrame(games_frame, fg_color="#D9D9D9", width=250, height=295, corner_radius=10)
            game_card.pack(side=ctk.LEFT, padx=30)

            game_label = ctk.CTkLabel(game_card, text=f"GAME {i + 1}", font=("Arial", 12, "bold"), text_color="black")
            game_label.place(relx=0.5, rely=0.4, anchor="center")

            price_label = ctk.CTkLabel(game_card, text="Name game\nPrice", font=("Arial", 10), text_color="black")
            price_label.place(relx=0.5, rely=0.7, anchor="center")

            heart_icon = ctk.CTkLabel(game_card, text="\u2764", font=("Arial", 14), text_color="#FF5900")
            heart_icon.place(relx=0.9, rely=0.9, anchor="center")

def libraryPageUI():
    # --------------DESIGN PÁGINA BIBLIOTECA ---------------------
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
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:" ",
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    discover_label = ctk.CTkLabel(topbar, text="MY LIBRARY", text_color="white", font=("Arial", 18))
    discover_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    categories = ["ACTION", "ADVENTURE", "RPG"]
    for idx, category in enumerate(categories):
        category_label = ctk.CTkLabel(app, text=category, font=("Arial", 14, "bold"), text_color="white")
        category_label.pack(anchor="w", padx=20, pady=10)
    
        games_frame = ctk.CTkFrame(app, fg_color="#101010")
        games_frame.pack(fill="x", padx=20, pady=10)

        for i in range(3):
            game_card = ctk.CTkFrame(games_frame, fg_color="#D9D9D9", width=250, height=295, corner_radius=10)
            game_card.pack(side=ctk.LEFT, padx=30)

            game_label = ctk.CTkLabel(game_card, text=f"GAME {i + 1}", font=("Arial", 12, "bold"), text_color="black")
            game_label.place(relx=0.5, rely=0.4, anchor="center")

            price_label = ctk.CTkLabel(game_card, text="Name game\nPrice", font=("Arial", 10), text_color="black")
            price_label.place(relx=0.5, rely=0.7, anchor="center")

            heart_icon = ctk.CTkLabel(game_card, text="\u2764", font=("Arial", 14), text_color="#FF5900")
            heart_icon.place(relx=0.9, rely=0.9, anchor="center")

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

    buttons = ["LIBRARY", "STORE", "DISCOVER"]
    for btn in buttons:
        if btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        elif btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:"",
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    settings_label = ctk.CTkLabel(topbar, text="SETTINGS", text_color="white", font=("Arial", 18))
    settings_label.pack(side=ctk.LEFT, padx=35, pady=50)

    user_info_frame = ctk.CTkFrame(app, width=875, height=450, fg_color="black")
    user_info_frame.place(x=370, y=160) 

    profile_circle = ctk.CTkButton(user_info_frame, width=100, height=100, corner_radius=77, fg_color="#FFA500", text="", hover_color="#FF5900")
    profile_circle.place(x=5, y=5)

    username_label = ctk.CTkLabel(user_info_frame, text="USERNAME", text_color="white", font=("Arial", 40, "bold"))
    username_label.place(x=120, y=15)

    personal_info = ctk.CTkLabel(user_info_frame, text="EMAIL:", text_color="white", font=("Arial", 22), justify="left")
    personal_info.place(x=120, y=65)

    change_password_button = ctk.CTkButton(user_info_frame, text="CHANGE PASSWORD", text_color="white", fg_color="#383838", font=("Arial", 22), hover_color="#5A5A5A", width=140, height=33)
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

    logoutBtn = ctk.CTkButton(app, text="LOGOUT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=191, height=52)
    logoutBtn.place(x=980, y=580)

    deleteAccountBtn= ctk.CTkButton(app, text="DELETE ACCOUNT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=800, height=55, command=lambda:deletePageUI())
    deleteAccountBtn.place(x=370, y=650)

def deletePageUI():
    # --------------DESIGN PÁGINA DELETE ---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()

    main_frame = ctk.CTkFrame(app, width=1180, height=732, fg_color="#2E2B2B", corner_radius=0)
    main_frame.pack(fill="both", expand=True)

    dlt_msg_label1 = ctk.CTkLabel(main_frame, text="THIS ACTION WILL DELETE YOUR ACCOUNT", 
                              font=ctk.CTkFont(size=45, weight="bold"), text_color="#FFA500")
    dlt_msg_label1.place(relx=0.5, rely=0.3, anchor="center")

    dlt_msg_label2 = ctk.CTkLabel(main_frame, text="PERMANENTLY!", 
                                font=ctk.CTkFont(size=50, weight="bold"), text_color="#FF4500")
    dlt_msg_label2.place(relx=0.5, rely=0.4, anchor="center")

    dlt_msg_label3 = ctk.CTkLabel(main_frame, text="ARE YOU SURE?", 
                                font=ctk.CTkFont(size=70, weight="bold"), text_color="#FFA500")
    dlt_msg_label3.place(relx=0.5, rely=0.55, anchor="center")

    button_frame = ctk.CTkFrame(main_frame, fg_color="#2E2B2B")
    button_frame.place(relx=0.5, rely=0.75, anchor="center")

    noBtn = ctk.CTkButton(button_frame, text="NO, I STILL WANNA PLAY!", fg_color="#D9D9D9", hover_color="#5A5A5A", width=300, height=60, border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=35, weight="bold"), command=lambda: settingsPageUI())
    noBtn.pack(side="left", padx=10)

    yesBtn = ctk.CTkButton(button_frame, text="YES, UNFORTUNATELY!", fg_color="#D9D9D9", hover_color="#5A5A5A", width=300, height=60, border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=35, weight="bold"), command=lambda: goodbyeUI() )
    yesBtn.pack(side="left", padx=10)
    
def goodbyeUI():
    # --------------DESIGN GOODBYE ---------------------
    #-----------------------------------------------------------------
    
    for widget in app.winfo_children():
        widget.destroy()

    goodbye_frame = ctk.CTkFrame(app, width=1180, height=732, fg_color="black")
    goodbye_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(450, 150))
    imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="")
    imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

    msg_welcome_label = ctk.CTkLabel(app, text="SEE YOU LATER!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_welcome_label.place(relx=0.5, rely=0.50, anchor="center")

    loading_canvas = tk.Canvas(app, width=120, height=120, bg="black", bd=0, highlightthickness=0)
    loading_canvas.place(relx=0.5, rely=0.65, anchor="center")

    update_loading_circle(loading_canvas, 0)

    msg_loading_label = ctk.CTkLabel(app, text="LOADING...", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_loading_label.place(relx=0.5, rely=0.80, anchor="center")

    app.after(5000, loginUI)

# --------------ECRÃ INICIAL ---------------------
#-----------------------------------------------------------------
imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(450, 150))
imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="")
imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

initial_msg_label = ctk.CTkLabel(app, text="WELCOME TO YOUR FAVORITE PLACE TO PLAY GAMES!",
                                  font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
initial_msg_label.place(relx=0.5, rely=0.5, anchor="center")

button_frame = ctk.CTkFrame(app, width=480, height=85, fg_color="#202020", corner_radius=15)
button_frame.place(relx=0.5, rely=0.6, anchor="center")  

initialBtn = ctk.CTkButton(button_frame, text="CLICK HERE IF YOU’RE ON!", text_color="black", fg_color="#FFA500",
                           font=ctk.CTkFont(size=20, weight="bold"), hover_color="#FF5900",
                           command=lambda:loginUI(), width=480, height=85)
initialBtn.place(relx=0.5, rely=0.5, anchor="center") 

# ---------------FIM DA FUNÇÃO DA APP ---------------------
#-----------------------------------------------------------------
app.mainloop()