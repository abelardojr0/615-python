par_ou_impar = lambda numero : "par" if numero % 2 == 0 else "ímpar"

numero = int(input("Digite um número: "))

print(par_ou_impar(numero))