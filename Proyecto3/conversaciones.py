class conversaciones:

    def __init__(self):
        self.nusuarios = 0

    def crearTabla(self,n):
        tabla1 = tablaC()
        self.tabla1 = tabla1
        self.tabla1.crear_tabla(n)
        self.nusuarios = n

    def agregarConversacion(self,c):
        if self.tabla1.tabla[hash(c.id)%(self.nusuarios)] != None:
            nodo = crearHashEntry(c.id,c)
            agregar_elem(tabla,nodo)
            return False
        else: 
            nodo = crearHashEntry(c.id,c)
            self.tabla1.agregar_elem(nodo)
            return True
        self.nusuarios = self.nusuarios

    def buscarConversacion(self,d):
        if self.tabla1.tabla[hash(d)%self.nusuarios] == None:
            return None
        else:
            return self.tabla1.tabla[hash(d)%self.nusuarios].head.string

class HashEntry:

    anterior = None
    siguiente = None
    def __init__(self,clave,string):

        self.clave = clave
        self.string = string
    def __str__(self):
        return str(self.clave) + str(self.string)

class tablaC:

    def crear_tabla(self,n):
        tabla = []
        for i in range(n):
            tabla.append(None)
        self.tabla = tabla
        

    def agregar_elem(self,nodo):

        if self.tabla[hash(nodo.clave)%len(self.tabla)] == None:
            lista = Dlist()         
            lista.inserta_al_principio(nodo)            
            self.tabla[hash(nodo.clave)%len(self.tabla)] = lista
        else:
            lista = self.tabla[hash(nodo.clave)%len(self.tabla)]
            nodo1 = lista.head
            condicional = True
            while nodo1 != None:
                if nodo1.clave == nodo.clave:
                    nodo1.clave = nodo.clave
                    condicional = False
                nodo1 = nodo1.siguiente
            if condicional:
                lista.inserta_al_final(nodo)
                self.tabla[hash(nodo.clave)%len(self.tabla)] = lista

def crearHashEntry(clave,string):
    nodo = HashEntry(clave,string)
    return nodo



class Dlist(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def inserta_adelante(self, nodo, nuevoNodo):
        nuevoNodo.anterior = nodo
        nuevoNodo.siguiente = nodo.siguiente
        if nodo.siguiente == None:
            self.last = nuevoNodo
        else:
            nodo.siguiente.anterior = nuevoNodo
        nodo.siguiente = nuevoNodo
        self.count += 1

    def inserta_atras(self, nodo, nuevoNodo):
        nuevoNodo.anterior = nodo.anterior

        nuevoNodo.siguiente = nodo

        if nodo.anterior == None:
            self.head = nuevoNodo
        else:
            nodo.anterior.siguiente = nuevoNodo
        nodo.anterior = nuevoNodo
        self.count += 1

    def inserta_al_principio(self, nodo):
        if self.head == None:
            self.head = nodo
            self.last = nodo
            nodo.anterior = None
            nodo.siguiente = None
            self.count += 1
        else:
            self.inserta_atras(self.head, nodo)

    def inserta_al_final(self, nodo):
        if self.last == None:
            self.inserta_al_principio(nodo)
        else:
            self.inserta_adelante(self.last, nodo)

    def eliminar(self, nodo):
        if nodo.anterior == None:
            self.head = nodo.siguiente
        else:
            nodo.anterior.siguiente = nodo.siguiente
        if nodo.siguiente == None:
            self.last = nodo.anterior
        else:
            nodo.siguiente.anterior = nodo.anterior
        self.count -= 1




        # PROBLEMA RESUELTO

    def mostrar(self):

        primero = self.head
        while primero != None:
            print(primero.dato.nombre)
            primero = primero.siguiente