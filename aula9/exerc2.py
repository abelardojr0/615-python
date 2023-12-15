from tkinter import *

box = Tk()
box.title("Média das notas")
box.geometry("300x300")

def calcular_media():
    nota1 = float(nota1_input.get())
    nota2 = float(nota2_input.get())
    media = (nota1 + nota2) / 2
    if media >= 7:
        resultado.configure(text=f"Aprovado com a média {media}", bg="green")
    else:
        resultado.configure(text=f"Reprovado com a média {media}", bg="red")



nota1_label = Label(text="Digite a primeira nota")
nota1_label.pack()

nota1_input = Entry()
nota1_input.pack()


nota2_label = Label(text="Digite a segunda nota")
nota2_label.pack()

nota2_input = Entry()
nota2_input.pack()


botao = Button(box, text="Calcular média", command=calcular_media)
botao.pack()

resultado = Label(text="")
resultado.pack()

box.mainloop()