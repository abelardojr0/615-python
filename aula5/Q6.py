concatena = lambda texto1, texto2 : f"{texto1}{texto2}" if len(texto1) > 5 and len(texto2) > 5 else "Error"


primeira_palavra = str(input("Digite a primeira palavra: "))
segunda_palavra = str(input("Digite a segunda palavra: "))


print(concatena(primeira_palavra, segunda_palavra))