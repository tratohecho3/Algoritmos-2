class Nodo:
    def __init__(self,dato):
        self.siguiente = None
        self.anterior = None
        self.dato = dato

class pila():

    def __init__(self):
        self.top = None
        self.head = None
        self.nelementos = 0
    def agregar(self,nodo):
        if self.nelementos == 0:
            self.top = nodo
            self.head = nodo
            self.nelementos = self.nelementos + 1
        else:
            nodo.anterior = self.top
            self.top.siguiente = nodo
            self.top = nodo
            self.nelementos = self.nelementos + 1
    def mostrar(self):
        aux = self.head
        for i in range(self.nelementos):
            print(aux.dato)
            aux = aux.siguiente

class chat:
    def __init__(self):
        self.id = None
        self.mensaje = pila()
    def crearChat(self,u1,u2):
        if u2.lower() < u1.lower():
            self.id = u2 + "-" + u1
        else:
            self.id = u1 + "-" + u2

    def agregarMensaje(self,nodo):
        self.mensaje.agregar(nodo)