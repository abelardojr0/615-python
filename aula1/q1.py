numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))


if numero1 >= numero2 and numero1 >= numero3:
    print(f"O {numero1} é o maior de todos")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"O {numero2} é o maior de todos")
else:
    print(f"O {numero3} é o maior de todos")

#VERSÃO ROUBADA NÃO FAÇA
# maior = max(numero1, numero2, numero3)
# print(f"O {maior} é o maior de todos")
