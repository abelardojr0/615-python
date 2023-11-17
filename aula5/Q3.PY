def maior_palavra(lista_de_palavras):
    maior = ""
    for item_da_vez in lista_de_palavras:
        if len(item_da_vez) > len(maior):
            maior = item_da_vez
    return maior

quantidade = int(input("Digite quantos nomes você quer inserir: "))

lista_de_nomes = []

for i in range(quantidade):
    nome = str(input("Digite um nome: "))
    lista_de_nomes.append(nome)


maior = maior_palavra(lista_de_nomes)
print(f"A maior palavra foi {maior}")

