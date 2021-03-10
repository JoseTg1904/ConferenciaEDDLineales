from .nodo import Nodo
from .archivo import crearGrafico

class ListaSimple:
    dot = ""

    # None se asemeja al uso de null en java
    def __init__(self):
        self.inicio = self.fin = None

    #Devuelve True si la lista esta vacia, False en caso contrario
    def estaVacia(self):
        return self.inicio == None

    def push(self, valor):
        if self.estaVacia():
            #Inicializando la pila
            self.fin = self.inicio = Nodo(None, valor)
        else:
            #agregando el valor al tope (inicio) de la pila
            self.inicio = Nodo(self.inicio, valor)
    
    def pop(self):
        if self.estaVacia():
            return "Lista vacia"
        # Si solo queda un valor en la pila hay que limpiar 
        # los punteros que apuntan al final e inico de la pila
        elif self.inicio == self.fin:
            aux = self.inicio 
            self.inicio = self.fin = None
            return "valor eliminado " + str(aux.getValor())
        else:
            #Retirando el elemento al tope (inicio) de la pila
            aux = self.inicio
            self.inicio = self.inicio.getSiguiente()
            return "valor eliminado " + str(aux.getValor())
        
    def enqueue(self, valor):
        if self.estaVacia():
            #Inicializando la cola
            self.inicio = self.fin = Nodo(None, valor)
        else:
            #Agregando el valor al final de la cola
            self.fin = Nodo(self.fin, valor)

    def dequeue(self):
        if self.estaVacia():
            return "Lista vacia"
        elif self.inicio == self.fin:
            aux = self.inicio
            self.inicio = self.fin = None
            return "valor eliminado " + str(aux.getValor())
        else:
            #Obteniendo el valor al tope (inicio) de la cola
            aux2 = self.inicio

            # Buscando el valor anterior al que se encuentra 
            # en el tope (inicio) de la cola
            aux = self.fin 
            while aux.getSiguiente() != aux2:
                aux = aux.getSiguiente()
            
            # El valor anterior al tope (inicio) es el nuevo tope
            # y apunto al vacio
            self.inicio = aux
            aux.setSiguiente(None)
            
            return "valor eliminado " + str(aux2.getValor())

    def graficar(self, tipo, nombre):
        # Haciendo uso de la variable global para el manejo del grafico
        global dot

        # Inicializando el documento de graphviz
        # node: se aplica a todos los nodos del grafico
        # style: da estilo al nodo, filled: nodo relleno
        # shape: forma del nodo 
        dot = "digraph grafico{\nnode [style = \"filled\" shape = \"box\"]\n"
        
        if tipo == "Cola":
            self.graficarCola()
        else:
            self.graficarPila()

        # Cierre del archivo de graphviz
        dot += "}"

        crearGrafico(dot, nombre)

    def graficarCola(self):
        global dot 
        
        dot += "rankdir = \"LR\"\n"
        
        if not self.estaVacia():
            # Iniciando el recorrido desde el final de la cola
            aux = self.fin

            # Recorriendo hasta que el nodo actual sea un nodo vacio
            while aux != None:
                # Validaciones unicamente para diferenciar los nodos inicio,
                # fin e internos, donde el inicio = rojo, fin = azul, interno = gris
                if aux == self.inicio:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"red\"]\n"
                elif aux == self.fin:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"blue\"]\n"
                else:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"gray\"]\n"
                
                # Validacion para verifcar que no se grafique un nulo cuando se llegue 
                # al final de la cola
                if aux.getSiguiente() != None:
                    dot += "\"" + str(aux) + "\" -> \"" + str(aux.getSiguiente()) + "\"\n" 
                
                # Obteniendo el nodo siguiente, esta es una forma de iterar 
                # similar a hacer un iterador++ en un ciclo for
                aux = aux.getSiguiente()
        
    def graficarPila(self):
        global dot

        if not self.estaVacia():
            # Iniciando el recorrido desde el tope (inicio) de la pila
            aux = self.inicio

            while aux != None:
                if aux == self.inicio:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"red\"]\n"
                elif aux == self.fin:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"blue\"]\n"
                else:
                    dot += "\"" + str(aux) + "\" [label = \"" + str(aux.valor) + "\" fillcolor = \"gray\"]\n"
                
                if aux.getSiguiente() != None:
                    dot += "\"" + str(aux) + "\" -> \"" + str(aux.getSiguiente()) + "\"\n" 
                
                aux = aux.getSiguiente()