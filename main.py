from clases import ListaSimple, ListaDoble

def inicial():
    # Pila
    pila = ListaSimple()
    pila.push(3)
    pila.push(4)
    pila.push(5)
    pila.push(2)
    pila.graficar("Pila", "pila1")
    print(pila.pop())
    pila.graficar("Pila", "pila2")
    
    # Cola
    cola = ListaSimple()
    cola.enqueue(3)
    cola.enqueue(5)
    cola.enqueue(6)
    cola.enqueue(2)
    cola.enqueue(1)
    cola.graficar("Cola", "cola1")
    print(cola.dequeue())
    print(cola.dequeue())
    cola.graficar("Cola", "cola2")
    
    # Lista
    doble = ListaDoble()
    doble.insertarOrdenado(4)
    doble.insertarOrdenado(6)
    doble.insertarOrdenado(3)
    doble.insertarOrdenado(9)
    doble.insertarOrdenado(5)
    doble.graficar(1, "doble1")
    doble.graficar(2, "doble2")
    print(doble.eliminarPorValor(4))
    print(doble.eliminarPorValor(3))
    print(doble.eliminarPorValor(5))
    print(doble.eliminarPorValor(1))
    doble.graficar(1, "doble3")
    doble.graficar(2, "doble4")

if __name__ == "__main__":
    inicial()