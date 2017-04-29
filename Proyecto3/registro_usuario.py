from usuario import *

class tablaRU:
    def crear_tabla(self, n):
        tabla = []
        for i in range(n):
            tabla.append(None)
        self.tabla = tabla


    def agregarUsuario(self, nodo):
        if not(self.buscar(nodo)):
            valor = hash(nodo.dato.nombre) % len(self.tabla)
            if self.tabla[valor] == None:
                lista = Dlist()
                lista.inserta_al_principio(nodo)
                self.tabla[hash(nodo.dato.nombre) % len(self.tabla)] = lista
                return True

            else:
                lista = self.tabla[valor]
                lista.inserta_al_principio(nodo)
                return True
        return False

    def eliminarUsuario(self,n):
        for i in range(len(self.tabla)):
            lista = self.tabla[i]
            if lista != None:
                nodo = lista.head
                while nodo != None:
                    if nodo.dato.nombre == n:
                        lista.eliminar(nodo)
                        return True
                    nodo = nodo.siguiente
        return False
    def mostrarRegistro(self):

        for i in range(len(self.tabla)):
            lista = self.tabla[i]
            if lista != None:
                nodo = lista.head
                while nodo != None:
                    print(nodo.dato.nombre)
                    nodo = nodo.siguiente
    def cargarUsuarios(self,archivo):
        f = open(archivo,'r')
        lista = []
        contador = 0
        condicional = True
        for linea in f:
            lista.append(linea.split("\t"))
            usuario1 = Usuario()
            lista_contactos = Lista()
            usuario1.crearUsuario(lista[contador][0],lista[contador][1],lista[contador][2],lista_contactos)
            nodo = Nodo(usuario1)

            self.agregarUsuario(nodo)
            contador += 1



        f.close()
    def login(self,nombre,password):
        for i in self.tabla:
            if i != None:
                primero = i.head
                while primero !=None:
                    if primero.dato.nombre == nombre and primero.dato.password == password:
                        return True,primero
                    primero = primero.siguiente

        return False,None
    def buscar(self,nodo):
        for i in self.tabla:
            if i != None:
                primero = i.head
                while primero !=None:
                    if primero.dato.nombre == nodo.dato.nombre :
                        return True
                    primero = primero.siguiente
        return False
    def buscar_nombre(self,nombre):
        for i in self.tabla:
            if i != None:
                primero = i.head
                while primero !=None:
                    if primero.dato.nombre == nombre:
                        return True,primero
                    primero = primero.siguiente
        return False,None

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