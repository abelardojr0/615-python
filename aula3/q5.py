lista = ["Banda", "Musica"]

dicionario = dict.fromkeys(lista)

dicionario["Banda"] = "Iron Maiden"
dicionario["Musica"] = "Powerslave"

print(dicionario.get("Banda", "Chave não existe"))
print(dicionario.get("Integrantes", "Chave não existe"))

print(dicionario)


