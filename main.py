from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0) #cria uma tela para colocar uma imagem sobreposta. Bg é a cor do fundo da imagem e highligh...é o tamanho da borda(nesse caso sem borda).
tomato_png = PhotoImage(file="tomato.png")  #importa a imagemdo ficheiro. O destino pode ser direto ou relativo
canvas.create_image(100, 112,image = tomato_png)  #cria a imagem e coloca no meio da tela... o eixo x é metade do valor e y também. Função imagem chama a variavel que recebeu o arquivo da imagem
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()



window.mainloop()