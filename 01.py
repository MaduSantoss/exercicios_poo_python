class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def apresentar(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e sou do sexo {self.sexo}")

p1 = Pessoa("Duda", 19, "feminino")
p1.apresentar()