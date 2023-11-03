animal = {
    "Especie": "Cachorro",
    "Raça": "Pinscher",
    "Idade": int(input("Digite a idade do cachorro: ")),
    "Adestrado": True
    }

if animal["Idade"] > 2:
    animal["Vacinado"] = True
else:
    animal["Adestrado"] = False

print(animal)