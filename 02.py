class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo indisponível!")
        else:
            self.saldo -= valor
    
    def mostrar_saldo(self):
        print(f"Saldo: {self.saldo}")

c1 = ContaBancaria("Duda")
c1.depositar(500)
c1.sacar(300)
c1.mostrar_saldo()
