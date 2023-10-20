sexo = str(input("""
Digite seu sexo:
F - Feminino
M - Masculino
""")).upper().strip()

if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
else:
    print("Sexo inválido")
