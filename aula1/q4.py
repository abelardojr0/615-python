letra = str(input("Digite uma letra: ")).lower()

if letra in "aeiou":
    print(f"{letra} é uma vogal")
elif letra in "bcdfghjklmnpqrstvxywz":
    print(f"{letra} é uma consoante")
else:
    print("Meu fi, digite uma LEEEEEETRA, conhece o alfabeto tu? ")

