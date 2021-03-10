class Nodo:
    def __init__(self, siguiente, valor):
        self.setSiguiente(siguiente)
        self.setValor(valor)

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setValor(self, valor):
        self.valor = valor

    def getSiguiente(self):
        return self.siguiente

    def getValor(self):
        return self.valor