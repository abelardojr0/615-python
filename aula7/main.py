from escola.matematica import *
from escola.portugues import *

lista_de_notas = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    lista_de_notas.append(nota)

print(f"O maior número é: {maior_numero(lista_de_notas)}")
print(f"O menor número é: {menor_numero(lista_de_notas)}")
print(f"A média dos números é: {media_numeros(lista_de_notas)}")


palavra = str(input("Digite uma palavra: "))
invertida = inverter_texto(palavra)

if palavra == invertida:
    print("É um palindromo")
else:
    print("Não é um palindromo")
print(f"A palavra digitada possui {contar_caracteres(palavra)}")
print(f"Número de vogais da palavra é: {contar_vogais_e_consoates(palavra)[0]}")
print(f"Número de vogais da palavra é: {contar_vogais_e_consoates(palavra)[1]}")