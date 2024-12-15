import customtkinter as ctk
from tkinter import messagebox

# Configuração inicial
ctk.set_appearance_mode("System")  # Modo de aparência: "Light", "Dark", ou "System"
ctk.set_default_color_theme("blue")  # Tema de cores: "blue", "green", ou "dark-blue"

# Função para o botão "Salvar"
def salvar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    
    if nome and email:
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")

# Função para o botão "Cancelar"
def cancelar():
    app.destroy()

# Criar a janela principal
app = ctk.CTk()
app.title("Formulário de Cadastro")
app.geometry("400x300")

# Container para os campos de entrada
frame_campos = ctk.CTkFrame(app)
frame_campos.pack(pady=20, padx=20, fill="both", expand=True)

# Rótulo e entrada para "Nome"
label_nome = ctk.CTkLabel(frame_campos, text="Nome:")
label_nome.pack(pady=5)
entry_nome = ctk.CTkEntry(frame_campos, placeholder_text="Digite seu nome")
entry_nome.pack(pady=5)

# Rótulo e entrada para "E-mail"
label_email = ctk.CTkLabel(frame_campos, text="E-mail:")
label_email.pack(pady=5)
entry_email = ctk.CTkEntry(frame_campos, placeholder_text="Digite seu e-mail")
entry_email.pack(pady=5)

# Container para os botões
frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10, padx=20, fill="x")

# Botão "Salvar"
botao_salvar = ctk.CTkButton(frame_botoes, text="Salvar", command=salvar_dados)
botao_salvar.pack(side="left", padx=10)

# Botão "Cancelar"
botao_cancelar = ctk.CTkButton(frame_botoes, text="Cancelar", command=cancelar)
botao_cancelar.pack(side="right", padx=10)

# Executar a aplicação
app.mainloop()
