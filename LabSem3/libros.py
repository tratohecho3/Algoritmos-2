#a = input("Como se llama el archivo con la lista de libros? ")


def leer(nombre):

	f = open(nombre, "r")
	autores = []
	libros = []
	contador = 0
	i = 0
	for linea in f.readlines():
		if i > 1:
			b = linea.split("	")
			autores.append(b[0])
			libros.append(b[1])
		i = i+1
	return autores, libros
print("baz"<"bas")