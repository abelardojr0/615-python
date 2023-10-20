frase = str(input("Digite uma frase: ")).lower().strip()

contador = 0
"A aula hoje foi top"

for letra in frase:
    if letra in "aeiou":
        contador = contador + 1

print(f"A frase digitada tem {contador} vogais")