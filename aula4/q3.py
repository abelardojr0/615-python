def calcular_hora(v,h):
    return v/h

valor = float(input("Digite o valor que você ganhou: "))
horas = int(input("Digite quantas horas trabalhou: "))

valor_hora = calcular_hora(valor, horas)

print(f"Você ganha {valor_hora:.2f} por hora trabalhada")

