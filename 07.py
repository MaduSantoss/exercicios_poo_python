from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio 

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

class Triangulo(Forma):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

formas = [
    Quadrado(4),
    Circulo(3),
    Triangulo(3, 3, 4)
]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
