def calcular_imc(p,a):
    return p / a ** 2

lista_de_imcs = []

for i in range (4):
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    
    imc = calcular_imc(peso, altura)

    lista_de_imcs.append(imc)

print(lista_de_imcs)