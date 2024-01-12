class Moto:
    def __init__(self, brand, model, cylinders, color):
        self.marca = brand
        self.modelo = model
        self.cilindradas = cylinders
        self.cor = color

    def ligar(self):
        return f"A moto {self.modelo} ligou"
    
    def ver_informacoes(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Cilindradas: {self.cilindradas}
        Cor: {self.cor}
    """

        
moto1 = Moto(brand="Honda", model="Bros", cylinders=160, color="preto")
moto2 = Moto(brand="Honda", model="Titan", cylinders=150, color="america")
moto3 = Moto(brand="Honda", model="Fan", cylinders=125, color="vermelho")


print(moto1.ligar())
print(moto2.ligar())
print(moto3.ligar())


print(moto2.ver_informacoes())
# moto4 = Moto("Honda", "bros", 160, "branco")


# print(moto1.marca)
# print(moto2.cilindradas, moto2.cor)
# print(moto3.marca, moto3.modelo, moto3.cilindradas, moto3.cor)


print(f"""
    Marca da primeira moto: {moto1.marca}

    Cilindradas da segunda moto: {moto2.cilindradas}
    Cor da segunda moto: {moto2.cor}

    Marca da terceira moto: {moto3.marca}
    Modelo da terceira moto: {moto3.modelo}
    Cilindradas da terceira moto: {moto3.cilindradas}
    Cor da terceira moto: {moto3.cor}
""")