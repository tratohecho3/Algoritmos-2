

#LASTIMOSAMENTE NO SE POR QUE ME DABA PROBLEMAS AL
# IMPORTAR LOS ARCHIVOS Y TUVE QUE PONER TODAS LAS FUNCIONES AQUI
# NUESTRAS FUNCIONES SIRVEN(LO PROBAMOS) PERO NO SUPIMOS HACER 
#EL CLIENTE ORDENAMIENTO :S
class HashEntry:

	anterior = None
	siguiente = None
	def __init__(self,clave,string):

		self.clave = clave
		self.string = string
	def __str__(self):
		return str(self.clave) + str(self.string)

class TablaHash:

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

	def agregar_clave_y_dato(self,clave1,string1):
		if self.tabla[hash(clave1)%len(self.tabla)] == None:
			lista = Dlist()
			nodo = crearHashEntry(clave1,string1)
			lista.inserta_al_principio(nodo)
			self.tabla[hash(clave1)%len(self.tabla)] = lista
		else:
			lista = self.tabla[hash(clave1)%len(self.tabla)]
			nodo1 = lista.head
			nodo = crearHashEntry(clave1,string1)
			condicional = True
			while nodo1 != None:
				if nodo1.clave == nodo.clave:
					nodo1.clave = nodo.clave
					condicional = False
				nodo1 = nodo1.siguiente
			if condicional:
				lista.inserta_al_final(nodo)
				self.tabla[hash(clave1)%len(self.tabla)] = lista

	
			

	def eliminar_con_clave(self,clave):
		for i in range(len(self.tabla)):
			lista = self.tabla[i]
			if lista != None:
				nodo = lista.head
				while nodo != None:
					if nodo.clave == clave:
						lista.eliminar(nodo)
						return nodo.string
					nodo = nodo.siguiente
		return None

	def buscar_con_clave(self,clave):
		for i in range(len(self.tabla)):
			lista = self.tabla[i]
			if lista != None:
				nodo = lista.head
				while nodo != None:
					if nodo.clave == clave:
						return nodo.string
					nodo = nodo.siguiente
		return None

	def mostrar(self):
		for i in range(len(self.tabla)):
			lista = self.tabla[i]
			if lista != None:
				nodo = lista.head
				while nodo != None:
					print((nodo.clave,nodo.string))
					nodo = nodo.siguiente

	def eliminar_elemento(self,nodo1):
		tipo = crearHashEntry(3,"tipo")
		if type(tipo) == type(nodo1):
			for i in range(len(self.tabla)):
				lista = self.tabla[i]
				if lista != None:	
					nodo = lista.head
					while nodo != None:
						if (nodo.clave == nodo1.clave) and (nodo.string == nodo1.string):
							lista.eliminar(nodo)
						nodo = nodo.siguiente


def crearHashEntry(clave,string):
	nodo = HashEntry(clave,string)
	return nodo





class Dlist(object):


    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def inserta_adelante(self,nodo,nuevoNodo):
        nuevoNodo.anterior = nodo
        nuevoNodo.siguiente = nodo.siguiente
        if nodo.siguiente == None:
            self.last = nuevoNodo
        else:
            nodo.siguiente.anterior = nuevoNodo
        nodo.siguiente = nuevoNodo
        self.count += 1



    def inserta_atras(self,nodo,nuevoNodo):
        nuevoNodo.anterior = nodo.anterior

        nuevoNodo.siguiente = nodo

        if nodo.anterior == None:
            self.head = nuevoNodo
        else:
            nodo.anterior.siguiente = nuevoNodo
        nodo.anterior = nuevoNodo
        self.count += 1


    def inserta_al_principio(self,nodo):
        if self.head == None:
            self.head = nodo
            self.last = nodo
            nodo.anterior = None
            nodo.siguiente = None
            self.count += 1
        else:
            self.inserta_atras(self.head,nodo)

    def inserta_al_final(self,nodo):
        if self.last == None:
            self.inserta_al_principio(nodo)
        else:
            self.inserta_adelante(self.last,nodo)

    def eliminar(self,nodo):
        if nodo.anterior == None:
            self.head = nodo.siguiente
        else:
            nodo.anterior.siguiente = nodo.siguiente
        if nodo.siguiente == None:
            self.last = nodo.anterior
        else:
            nodo.siguiente.anterior = nodo.anterior
        self.count -= 1     

    


#PROBLEMA RESUELTO
archivo = open("diccionario.txt","r")
contador = 0
tabla = TablaHash()

linea1 = archivo.readline()
tabla.crear_tabla(int(linea1))
lista = Dlist()


for linea in archivo.readlines():
	if contador >0:
		nodo = crearHashEntry(linea.rstrip('\n'),linea.rstrip('\n'))
		tabla.agregar_elem(nodo)

	contador += 1

while True:
	try:
		password = input("ingrese su password ")
		if len(password) >= 8:
			a =tabla.buscar_con_clave(password)
			if a != None:
				raise NameError('')
			break				
		else:
			print("Ingrese una password con al menos 8 digitos")

	except:
		print("Tu password coincide con alguna palabra no permitida")



