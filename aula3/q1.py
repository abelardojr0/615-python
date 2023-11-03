pessoa = {"Nome": "Abel",
          "Idade": 28,
          "Altura": 1.79,
          "Habilitacao": True
        }

print(f"O dicionário possui {len(pessoa)} chaves")

lista_chaves = list(pessoa)

for chave in lista_chaves:
    print(chave)
