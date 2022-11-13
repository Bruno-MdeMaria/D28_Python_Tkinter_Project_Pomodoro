from tkinter import *
import math  #para função matemática do timer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repets = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- MECANISMO DE TEMPO ------------------------------- # 
def iniciar_timer():
    global repets
    repets +=1

    work_seg = WORK_MIN *60
    short_break_seg = SHORT_BREAK_MIN * 60
    long_break_seg = LONG_BREAK_MIN * 60
    
    #se a variavel "repets" for a 1°/3°/5°/7°:
    contagem_regresiva(work_seg)  #Contagem regressiva inicia com o tempo de trabalho = 25 minutos
    if repets % 8 == 0    # se a repetição dividida por 8 for igual a resto 0(ou seja na outava repeticao):
        contagem_regresiva(long_break_seg) #o relógio deverá 






# ---------------------------- MECANISMO DE CONTAGEM DECRECENTE------------------------------- # 
def contagem_regresiva(contagem):
    contagem_minutos = math.floor(contagem / 60)
    contagem_seg = contagem % 60
    if contagem_seg < 10:
        contagem_seg = f"0{contagem_seg}"  #para deixar da forma os segundos 5:00 e 0:09, 0:08.
    canvas.itemconfig(tempo_text, text=f"{contagem_minutos}:{contagem_seg}")
    if contagem >0:
        window.after(1000, contagem_regresiva, contagem-1)  #a janela depois(after) de 1000 milesegundos(1seg) deve abrir a função 




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=GREEN)


#TÍTULO
titulo_label = Label(text="Timer", foreground= RED, bg=GREEN, font=(FONT_NAME, 40, "bold"))
titulo_label.grid(column=1, row=0)

#IMAGEM CENTRAL DO TOMATE E RELOGIO:
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0) #cria uma tela para colocar uma imagem sobreposta. Bg é a cor do fundo da imagem e highligh...é o tamanho da borda(nesse caso sem borda).
tomato_png = PhotoImage(file="tomato.png")  #importa a imagem do ficheiro. O destino pode ser direto ou relativo
canvas.create_image(100, 112,image = tomato_png)  #cria a imagem e coloca no meio da tela... o eixo x é metade do valor e y também. Função imagem chama a variavel que recebeu o arquivo da imagem
tempo_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) #o relogio zerado é uma str informado no "text= 00:00"
canvas.grid(column=1, row=1)


#BOTAO INICIAR e RESET:
button_start = Button(text="Start", highlightthickness=0, command= iniciar_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0)
button_reset.grid(column=2,row=2)

#MARCA DE CHACAGEM:
check_marks = Label(text=" ✔ " , fg="#379237", bg=GREEN)
check_marks.grid(column=1, row=3)
window.mainloop()