from nodo import Nodo
class ArbolBinario:
	def __init__(self):
		self.raiz = None
	

	def crearArbol(self):
		self.raiz = None

	def agregar_elem(self,string):
		nodo = Nodo()
		nodo.crearNodo(string)	
		if self.raiz == None:
			self.raiz = nodo
		else:
			x = self.raiz
			aux = x
			while x != None:
				aux = x
				if string < x.dato: 
					x = x.izq
				elif string > x.dato:
					x = x.der
				else:
					return False
			if aux.dato < string:
				aux.der = nodo
			else:
				aux.izq = nodo
		return True
	def buscar(self,string):

		if self.raiz == None:
			return False
		else:
			aux = Nodo()
			aux.crearNodo(self.raiz.dato)
			aux.izq = self.raiz.izq
			aux.der = self.raiz.der
			while self.raiz != None:
				if self.raiz.dato == string:
					self.raiz = aux
					self.raiz.der = aux.der
					self.raiz.izq = aux.izq
					return True
				else:
					if string < self.raiz.dato:
						self.raiz = self.raiz.izq
					else:
						self.raiz = self.raiz.der
		self.raiz = aux
		self.raiz.der = aux.der
		self.raiz.izq = aux.izq
		return False
	def minimo(self):
		x = self.raiz
		if x.dato == None:
			return None
		while x != None:
			aux = Nodo()
			aux.crearNodo(x.dato)
			x = x.izq
		return aux.dato
	def maximo(self):
		x = self.raiz
		if x.dato == None:
			return None
		while x != None:
			aux = Nodo()
			aux.crearNodo(x.dato)
			x = x.der
		return aux.dato
	def eliminar_elem(self,string):
		x = self.raiz
		y = x
		if  not(self.buscar(string)):
			return False
		elif x.izq == None and x.der == None:
			self.raiz = None
			return True
		else:
			while x != None:
				if x.dato == string:
					aux = Nodo()
					aux.crearNodo(x.dato)

					if x.izq == None and x.der == None:
						if x.dato < y.dato:
							print(x.dato,y.dato)
							y.izq = None
						else: 
							y.der = None
						break

					if x.izq == None and x.der != None:
						if x.dato < y.dato:
							y.izq = x.der
						else:
							y.der = x.der
						break

					if x.izq != None and x.der== None:
						if x.dato < y.dato:
							y.izq = x.izq
						else:
							y.der = x.izq
						break

					if x.izq != None and x.der != None:
						if x.dato < y.dato:
							pass


				else:
					y = x
					if string < x.dato:
						x = x.izq
					else:
						x = x.der
	def pre_orden(self,raiz):
		if self.raiz == None:
			print("El arbol se encuentra vacio")
		if raiz != None:
			print(raiz.dato)
			self.pre_orden(raiz.izq)
			self.pre_orden(raiz.der)








