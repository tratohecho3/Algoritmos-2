class Nodo:
    def __init__(self,dato):
        self.siguiente = None
        self.anterior = None
        self.dato = dato

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar_al_frente(self,nodo,nuevo):
        nuevo.anterior = nodo.anterior
        nuevo.siguiente = nodo
        if nodo.anterior == None:
            self.head = nuevo
        else:
            nodo.anterior.siguiente = nuevo
        nodo.anterior = nuevo


    def insertar(self,nodo):
        insertar = False
        if self.head == None:
            self.head = nodo
            self.tail = nodo

        else:
            primero = self.head
            while primero != None:
                if nodo.dato.nombre < primero.dato.nombre:
                    self.insertar_al_frente(primero,nodo)
                    insertar = True
                    break
                else:

                    if primero.siguiente != None:
                        primero = primero.siguiente
                    else:
                        break

            if not(insertar):
                primero.siguiente = nodo
                nodo.anterior = primero
                nodo.siguiente = None
                self.tail = nodo
    def mostrar(self):
        primero = self.head
        while primero != None:
            print((primero.dato.nombre,primero.dato.telefono))
            primero = primero.siguiente
    def buscar_nombre(self,nombre):
        primero = self.head
        while primero != None:
            if primero.dato.nombre == nombre:
                return True,primero
            primero = primero.siguiente
        return False,None

    def buscar(self,nodo):
        primero = self.head
        while primero != None:
            if nodo == primero:
                return True
            else:
                primero = primero.siguiente
        return False

    def eliminar(self,nombre):
        primero = self.head
        if primero != None:
            if primero.dato.nombre == nombre:
                if primero.siguiente != None:
                    primero.siguiente.anterior = None
                    self.head = primero.siguiente
                    return True
                else:
                    self.head = None
                    return True
            else:
                primero = primero.siguiente
                while primero != None:
                    if primero.dato.nombre == nombre:
                        if primero.siguiente != None:
                            primero.anterior.siguiente = primero.siguiente
                            primero.siguiente.anterior = primero.anterior
                            return True
                        else:
                            primero.anterior.siguiente = primero.siguiente
                            primero.anterior = self.tail
                            return True
                    primero = primero.siguiente
        return False

class Usuario:
    def __init__(self):
        self.nombre = None
        self.password = None
        self.telefono = None
        self.contactos = None

    def crearUsuario(self,nombre,password,telefono,contactos):

        self.nombre = nombre
        self.password = password
        self.telefono = telefono
        self.contactos = contactos

    def agregarContacto(self,u):
        nodo = Nodo(u)
        if self.contactos.buscar(nodo):
            return False
        else:
            self.contactos.insertar(nodo)
            return True
    def eliminarContacto(self,n):
        if self.contactos.eliminar(n):
            return True
        else:
            return False
    def mostrarContactos(self):
        self.contactos.mostrar()
