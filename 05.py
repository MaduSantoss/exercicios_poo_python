class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if preco < 0:
            print("Preço inválido")
        else:
            self.__preco = preco
        

p = Produto("Caneta", 3.5)
print(p.nome)  
print(p.preco) 

p.preco = -10  
p.preco = 5.0     
print(p.preco) 
