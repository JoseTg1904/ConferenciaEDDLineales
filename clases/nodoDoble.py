class NodoDoble:
    def __init__(self, anterior, siguiente, valor):
        self.setAnterior(anterior)
        self.setSiguiente(siguiente)
        self.setValor(valor)

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
    
    def setValor(self, valor):
        self.valor = valor

    def setAnterior(self, anterior):
        self.anterior = anterior

    def getSiguiente(self):
        return self.siguiente
    
    def getValor(self):
        return self.valor
    
    def getAnterior(self):
        return self.anterior