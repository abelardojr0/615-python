from tkinter import *

caixinha = Tk()
caixinha.title("Aula 1 TKinter")
caixinha.geometry("400x400")
caixinha.configure(bg="#1b1833")

def mostrar_nome():
    print(nome_input.get())

nome = Label(text="Digite seu nome", bg="#77767c", fg="#e2e2e2")
nome.pack()

nome_input = Entry()
nome_input.pack()

botao = Button(caixinha, text="Enviar", command=mostrar_nome)
botao.pack()

caixinha.mainloop()