import customtkinter as ctk

# Função para desenhar o gráfico
def draw_bar_chart():
    data = [10, 20, 30, 40, 50]  # Dados para o gráfico de barras
    labels = ['A', 'B', 'C', 'D', 'E']  # Rótulos para as barras
    
    canvas.delete("all")  # Limpar qualquer desenho anterior no canvas

    bar_width = 40  # Largura das barras
    spacing = 30  # Espaçamento entre as barras

    # Desenhando as barras
    for i, value in enumerate(data):
        x1 = i * (bar_width + spacing) + 50  # Posição inicial da barra no eixo X
        y1 = 300  # Posição inicial da barra no eixo Y
        x2 = x1 + bar_width  # Posição final da barra
        y2 = y1 - value  # Posição final no eixo Y (altura das barras)

        # Desenhando a barra no canvas
        canvas.create_rectangle(x1, y1, x2, y2, fill="orange")
        
        # Adicionando o rótulo da barra
        canvas.create_text(x1 + bar_width / 2, y1 + 20, text=labels[i], fill="white")
    
    # Adicionando os valores nas barras
    for i, value in enumerate(data):
        canvas.create_text(i * (bar_width + spacing) + 50 + bar_width / 2, y1 - value - 10, 
                           text=str(value), fill="black")

# Criando a interface
app = ctk.CTk()
app.geometry("600x400")
app.title("Gráfico de Barras com CustomTkinter")

# Canvas onde o gráfico será desenhado
canvas = ctk.CTkCanvas(app, width=500, height=300, bg="black")
canvas.pack(pady=20)

# Botão para desenhar o gráfico
draw_button = ctk.CTkButton(app, text="Desenhar Gráfico", command=draw_bar_chart)
draw_button.pack()

# Iniciando a interface
app.mainloop()
