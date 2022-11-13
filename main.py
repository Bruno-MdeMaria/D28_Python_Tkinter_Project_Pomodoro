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

canvas = Canvas(width=200, height=224) #cria uma tela para colocar uma imagem sobreposta
tomato_png = PhotoImage(file="tomato.png")  #importa a imagemdo ficheiro. O destino pode ser direto ou relativo
canvas.create_image(100, 112,image = tomato_png)  #cria a imagem e coloca no meio da tela... o eixo x é metade do valor e y também. Função imagem chama a variavel que recebeu o arquivo da imagem
canvas.pack()



window.mainloop()