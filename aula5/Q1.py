def maior_dos_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    else:
        return num1




numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = maior_dos_tres(numero1,numero2,numero3)

print(f"O maior número dividido por 2 é {maior/2}")