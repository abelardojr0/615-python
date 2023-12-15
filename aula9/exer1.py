from tkinter import *

janelinha = Tk()
janelinha.title("Maior idade")
janelinha.geometry("200x200")


def maior_idade():
    idade = 2023 - int(ano_input.get())
    if idade >=18:
        resultado.configure(text="Resultado: Maior de Idade")
    else:
        resultado.configure(text="Resultado: Menor de Idade")


ano_label = Label(text="Digite o ano que você nasceu")
ano_label.pack()

ano_input = Entry()
ano_input.pack()


botao = Button(janelinha, text="Conferir idade", command=maior_idade)
botao.pack()

resultado = Label(text="Resposta: ")
resultado.pack()


janelinha.mainloop()