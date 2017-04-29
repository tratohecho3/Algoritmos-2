

class NodoLista():
    def __init__(self, e, s, a):
        self.elemento = e
        self.siguiente = s
        self.anterior = a

    def __str__(self):
        cadena = "Elemento: " + str(self.elemento) + ", Anterior: " + str(self.anterior) + ", Siguiente: " + str(self.siguiente)
        return cadena
class ListaReproduccion():
    def __init__(self):
        self.proxima = None
        self.numero_nodos= 0


    def agregar(self,e):
        if self.numero_nodos == 0:
            self.agregar_final(e)
        else:
            self.proxima = self.proxima.anterior
            self.proxima.anterior.siguiente = e
            e.anterior = self.proxima.anterior
            e.siguiente = self.proxima
            self.proxima.anterior = e
            self.numero_nodos += 1


    def mostrar(self):
        if self.numero_nodos == 0:
            print("===========================================")
            print("La lista de reproduccion esta vacia.")
            print("===========================================") 
            return False
        else:
            i = 1
            aux = self.proxima
            vacio = True
            print("===========================================")
            while i <= self.numero_nodos:
                print(self.proxima.elemento.titulo)
                self.proxima = self.proxima.siguiente
                vacio = False
                i = i + 1
            print("===========================================")
            self.proxima = aux
            return True
    def agregar_final(self,e):
        if self.numero_nodos == 0:
            self.proxima = e
            e.anterior = e
            e.siguiente = e
            self.numero_nodos += 1

        else:
            e.anterior = self.proxima
            e.siguiente = self.proxima.siguiente
            self.proxima.siguiente.anterior = e
            self.proxima.siguiente = e
            self.proxima = e
            self.numero_nodos += 1

    def ordenar_titulo(self):
        pass

    def ordenar_artista(self):
        pass

    def eliminar(self,tituloCancion):
        eliminado = False
        if self.numero_nodos == 0:
            print("===========================================")
            print("No se pueden eliminar elementos porque la lista de reproduccion esta vacia.")
            print("===========================================")

        elif self.numero_nodos != 0:
            aux = self.proxima 
            aux2 = aux.elemento.titulo
            if self.numero_nodos == 1:  
                self.proxima = None
                self.numero_nodos = self.numero_nodos - 1 
                return 
            if aux2 == tituloCancion:
                aux.anterior.siguiente = aux.siguiente
                aux.siguiente.anterior = aux.anterior
                self.numero_nodos = self.numero_nodos -1
                print("Hola")
                eliminado = True
            else:
                self.proxima = self.proxima.siguiente
                while self.proxima != aux:
                    if self.proxima.elemento.titulo == tituloCancion:
                        self.proxima.anterior.siguiente = self.proxima.siguiente
                        self.proxima.siguiente.anterior = self.proxima.anterior
                        self.numero_nodos = self.numero_nodos - 1
                        print("Hola")
                        eliminado = True
                        break
                    else:
                        self.proxima = self.proxima.siguiente
            self.proxima = aux
            if eliminado == False:
                print("===========================================")
                print("El elemento a eliminar no se encuentra en la lista de reproduccion")
                print("===========================================")
        else:
            print("La lista esta vacia, no se pueden eliminar elementos.")

    def __str__(self):
        if self.proxima != None:
            primero = self.proxima.siguiente
        else:
            primero = None
        if primero != None:
            cadena = primero.elemento.titulo 
            self.proxima = primero.siguiente
            while self.proxima != primero:
                cadena += " " + self.proxima.elemento.titulo
                self.proxima = self.proxima.siguiente
            return cadena
        else:
            return "Vacio"

def merge_sort1(A,p,r):
    if p < r:
        q = int((p+r)/2)
        merge_sort1(A,p,q)
        merge_sort1(A,q+1,r)
        merge(A,p,q,r)
    return A
def merge(A,p,q,r):
    n = q - p + 1
    m = r - q
    lista1 = ListaReproduccion()
    lista2 = ListaReproduccion()
    primer_elemento = A.proxima
    lista1.agregar_final(primer_elemento)
    primer_elemento.anterior = primer_elemento
    primer_elemento.siguiente = primer_elemento
    primer_elemento = A.proxima.siguiente
    i = 1
    while primer_elemento != A.proxima:
        if i <= n:
            lista1.agregar_final(primer_elemento)
            primer_elemento = A.proxima.siguiente
        else:
            lista2.agregar_final(primer_elemento)
            primer_elemento = A.proxima.siguiente
        i = i + 1
    print(lista1)
    print(lista2)
    i,j = 0,0
    primero_l1 = lista1.proxima
    primero_l2 = lista2.proxima

    primero_en_a = A.proxima
    siguiente_en_a = primero_en_a.siguiente
    A.eliminar(primero_en_a.elemento.titulo)
    k = 1
    while k  <= A.numero_nodos + 1:
        aux = siguiente_en_a.siguiente
        A.eliminar(siguiente_en_a.elemento.titulo)
        siguiente_en_a = aux
        k = k + 1


    """
    for k in range(lista.numero_nodos):
        print(A)
        if primero_l1.elemento.es_menor_artista(primero_l2):
            A.agregar_final(primero_l1)
            primero_l1 = primero_l1.siguiente
        else:
            A.agregar_final(primero_l2)
            primero_l2 = primero_l2.siguiente
    """
    return A

