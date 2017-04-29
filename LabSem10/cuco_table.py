from arrayT import ArrayT
from cuco_entry import *
import hashlib

def hash1(clave):
	h = hashlib.sha256(clave.encode())
	return int(h.hexdigest(),base=16)

def hash2(clave):
	h = hashlib.md5(clave.encode())
	return int(h.hexdigest(),base=16)


class CucoTable():

	def crearCucoTabla(self,n):
		self.arreglo = ArrayT(n)

	def agregar(self,clave,valor):

		cuco = CucoEntry()
		cuco.crearCucoEntry(clave,valor)
		i = 1
		while i <= len(self.arreglo):

			if i%2 == 1:
				if self.arreglo[hash1(cuco.clave)%len(self.arreglo)] == None:
					self.arreglo[hash1(cuco.clave)%len(self.arreglo)] = cuco 
					return 1
				else:
					aux = self.arreglo[hash1(cuco.clave)%len(self.arreglo)]
					self.arreglo[hash1(cuco.clave)%len(self.arreglo)] = cuco
					cuco = aux
			else:
				if self.arreglo[hash2(cuco.clave)%len(self.arreglo)] == None:
					self.arreglo[hash2(cuco.clave)%len(self.arreglo)] = cuco 
					return 1
				else:
					aux = self.arreglo[hash2(cuco.clave)%len(self.arreglo)]
					self.arreglo[hash2(cuco.clave)%len(self.arreglo)] = cuco
					cuco = aux
			i = i + 1
		self.rehash()
		return None

	def rehash(self):
		n = len(self.arreglo)
		rehash = ArrayT(2*n)
		for i in range(n):
			rehash[i] = self.arreglo[i]
		self.arreglo = rehash
	def eliminar(self,clave):
		for i in range(len(self.arreglo)):
			if self.arreglo[i] != None:
				if self.arreglo[i].clave == clave:
					string = self.arreglo[i].valor
					self.arreglo[i] = None

					return string
		return None
	def buscar(self,clave):
		for i in range(len(self.arreglo)):
			if self.arreglo[i] != None:
				if self.arreglo[i].clave == clave:
					string = self.arreglo[i].valor
					print(string)
					return string
		return None

	def mostrar(self):
		for i in range(len(self.arreglo)):
			if self.arreglo[i] != None:
				print((self.arreglo[i].clave,self.arreglo[i].valor))
