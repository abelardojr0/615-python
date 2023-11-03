colecao_cores = {"Amarelo", "Azul", "Vermelho", "Verde"}

lista_novas_cores = []

while True:
    cor = str(input("Digite uma nova cor: "))

    if cor == "sair":
        break

    lista_novas_cores.append(cor)

colecao_cores.update(lista_novas_cores)

print(colecao_cores)
