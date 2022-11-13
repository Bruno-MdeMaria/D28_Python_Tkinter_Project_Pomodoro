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

# ---------------------------- MECANISMO DE CONTAGEM DECRECENTE------------------------------- # 
def contagem_regresiva(contagem):
    print(contagem)
    window.after(1000, contagem_regresiva, contagem-1)  #a janela depois(after) de 1000 milesegundos(1seg) deve abrir a função 







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=GREEN)
contagem_regresiva(contagem=5)

#TÍTULO
titulo_label = Label(text="Timer", foreground= RED, bg=GREEN, font=(FONT_NAME, 40, "bold"))
titulo_label.grid(column=1, row=0)

#IMAGEM CENTRAL DO TOMATE E RELOGIO:
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0) #cria uma tela para colocar uma imagem sobreposta. Bg é a cor do fundo da imagem e highligh...é o tamanho da borda(nesse caso sem borda).
tomato_png = PhotoImage(file="tomato.png")  #importa a imagemdo ficheiro. O destino pode ser direto ou relativo
canvas.create_image(100, 112,image = tomato_png)  #cria a imagem e coloca no meio da tela... o eixo x é metade do valor e y também. Função imagem chama a variavel que recebeu o arquivo da imagem
canvas.create_text(100, 130, text=contagem_regresiva, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#BOTAO INICIAR e RESET:
button_start = Button(text="Start", highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0)
button_reset.grid(column=2,row=2)

#MARCA DE CHACAGEM:
check_marks = Label(text=" ✔ " , fg="#379237", bg=GREEN)
check_marks.grid(column=1, row=3)
window.mainloop()