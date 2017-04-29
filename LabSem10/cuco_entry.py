class CucoEntry:
	def crearCucoEntry(self,clave,valor):
		self.clave = clave
		self.valor = valor

	def __str__(self):
		cadena = self.clave + " " + self.valor
		return cadena
