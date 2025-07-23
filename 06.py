class Animal:
    def falar(self):
        print("Animal faz som genérico")

class Cachorro(Animal):
    def falar(self):
        print("Au au")

class Gato(Animal):
    def falar(self):
        print("Miau")

animais = [Cachorro(), Gato(), Gato(), Cachorro()]

for animal in animais:
    animal.falar()
