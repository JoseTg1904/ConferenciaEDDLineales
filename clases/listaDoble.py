from .nodoDoble import NodoDoble
from .archivo import crearGrafico

class ListaDoble:
    dot = ""

    def __init__(self):
        self.inicio = self.fin = None

    def estaVacia(self):
        return self.inicio == None

    # Insercion ordenada dejando los valores mayores hacia el 
    # inicio y los valores menores hacia el fin
    def insertarOrdenado(self, valor):
        if self.estaVacia():
            self.inicio = self.fin = NodoDoble(None, None, valor)
        else:
            # Recorrer desde el inicio de la lista 
            aux = self.inicio 

            # Verificador de insercion del valor
            bandera = False
            
            while aux != None:
                if valor > aux.getValor():
                    # Suponiendo que el nodo se inserta enmedio de dos nodos
                    # existentes, el nuevo nodo al ser mayor su anterior 
                    # es el nodo actual y el siguiente es el que era el 
                    # siguiente del actual
                    nuevo = NodoDoble(aux, aux.getSiguiente(), valor)

                    # El nodo actual ahora apunta hacia el nuevo nodo
                    aux.setSiguiente(nuevo)

                    # En el caso de que el nodo actual sea el inicio
                    # el nuevo nodo ahora es el inicio
                    if aux == self.inicio:
                        self.inicio = nuevo
                    else:
                        # En caso de que no es el inicio significa que 
                        # tiene un nodo siguiente por lo tanto a ese 
                        # siguiente hay que cambiarle su anterior que
                        # ahora es el nuevo nodo
                        aux.getSiguiente().setAnterior(nuevo)

                    bandera = True

                    # Salirse del ciclo por que ya se realizo la insercion 
                    # del nuevo nodo
                    break

                aux = aux.getSiguiente()

            # Si la insercion no se diera quiere decir que el valor ingresado
            # es menor a todos los existentes por lo tanto va al final
            if not bandera:
                nuevo = NodoDoble(None, self.fin, valor)
                self.fin.setAnterior(nuevo)
                self.fin = nuevo

    def eliminarPorValor(self, valor):
        if self.estaVacia():
            return "Lista vacia"
        else:
            # Comenzando a recorrer desde el fin de la lista
            aux = self.fin
            bandera = False

            while aux != None:
                if aux.getValor() == valor:
                    # Si el nodo a eliminar corresponde al inicio y fin
                    # de la lista reiniciar estos
                    if aux == self.fin and aux == self.inicio:
                        self.inicio = self.fin = None
                    else:
                        # Verificando que el nodo a eliminar sea un nodo interno
                        if aux.getAnterior() != None and aux.getSiguiente() != None:
                            aux.getAnterior().setSiguiente(aux.getSiguiente())
                            aux.getSiguiente().setAnterior(aux.getAnterior())
                        else:
                            # Verificando los casos especiales del inicio y fin
                            if aux == self.inicio:
                                aux.getAnterior().setSiguiente(None)
                                self.inicio = aux.getAnterior()
                            else:
                                aux.getSiguiente().setAnterior(None)
                                self.fin = aux.getSiguiente()
                    
                    bandera = True

                aux = aux.getSiguiente()
            
            if bandera:
                return f"el valor: {valor}, fue eliminado"

            return "el valor no estaba en la lista :c"

    def graficar(self, tipo, nombre):
        global dot

        dot = "digraph grafico{\nnode [style = \"filled\" shape = \"box\"]\n"
        
        if tipo == 1:
            self.recorridoinicioFin()
        else:
            self.recorridofinInicio()
        
        dot += "}"

        crearGrafico(dot, nombre)

    def recorridoinicioFin(self):
        global dot

        if not self.estaVacia():
            aux = self.inicio
            while aux != None:
                if aux == self.inicio:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"red\"]\n"
                elif aux == self.fin:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"blue\"]\n"
                else:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"gray\"]\n"
                
                if aux.getAnterior() != None:
                    dot += "\"" + str(aux) + "\" -> \"" + str(aux.getAnterior()) + "\"\n"
                
                if aux.getSiguiente() != None:
                    dot += "\"" + str(aux) + "\" -> \"" + str(aux.getSiguiente()) + "\"\n" 
                
                aux = aux.getAnterior()

    def recorridofinInicio(self):
        global dot
        
        if not self.estaVacia():
            aux = self.fin
            while aux != None:
                if aux == self.inicio:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"red\"]\n"
                elif aux == self.fin:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"blue\"]\n"
                else:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"gray\"]\n"
                
                if aux.getAnterior() != None:
                    dot += "\"" + str(aux) + "\" -> \"" + str(aux.getAnterior()) + "\"\n"
                
                if aux.getSiguiente() != None:
                    dot += "\"" + str(aux) + "\" -> \"" + str(aux.getSiguiente()) + "\"\n" 
                
                aux = aux.getSiguiente()