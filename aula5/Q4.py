from datetime import datetime

maioridade = lambda idade : "maior de idade" if idade >= 18 else "menor de idade"

ano_nascimento = int(input("Digite o ano que você nasceu: "))

ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

print(maioridade(idade))