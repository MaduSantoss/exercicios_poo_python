class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario 
    
    def calcular_pagamento(self):
        return self.salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
    
    def calcular_pagamento(self):
        return self.salario + self.bonus
    
f1 = Funcionario("Carlos", 3000)
g1 = Gerente("Ana", 5000, 2000)

print(f1.nome, "vai receber:", f1.calcular_pagamento())
print(g1.nome, "vai receber:", g1.calcular_pagamento())
