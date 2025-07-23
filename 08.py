class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca         
        self._modelo = modelo       
        self._velocidade = 0        

    def acelerar(self, valor):
        self._velocidade += valor

    def frear(self, valor):
        self._velocidade -= valor
        if self._velocidade < 0:
            self._velocidade = 0

    def mostrar_info(self):
        print(f"Marca: {self._marca} | Modelo: {self._modelo} | Velocidade: {self._velocidade} km/h")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self._num_portas = num_portas    

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Portas: {self._num_portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo      

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self._tipo}")

# Testando
c = Carro("Ford", "Mustang", 2)
m = Moto("Honda", "CBR500R", "esportiva")

c.acelerar(50)
c.frear(10)
c.mostrar_info()

m.acelerar(100)
m.frear(30)
m.mostrar_info()
