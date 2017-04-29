from arrayT import ArrayT

def contar(nombre):
	f = open(nombre, "r")
	contador = 0
	for linea in f.readlines():
		contador = contador + 1
	return contador

def leer(nombre,contador):
	f = open(nombre, "r")
	autores = ArrayT(contador-1)
	libros = ArrayT(contador-1)
	i = 0
	
	for linea in f.readlines():
		if i >= 1:
			b =[]
			b = linea.split("	")
			autores[i-1] = b[0]
			libros[i-1] =b[1].strip("\n")
		i = i+1
			

	return autores, libros
contador=contar("entrada.txt")
autores=leer("entrada.txt",contador)[0]
libros= leer("entrada.txt",contador)[1]

def merge_sort(a):
    z = ArrayT(len(a))
    k = 1
    N = len(a)
    while k < N:
        
        d,b,c = 0, k, min(2*k,N)

        while b < N:
            p,q,r = d,b,d
            

            while p!=b and q!=c:
                #print(a[p],a[q])
                if a[p] <= a[q]:
                    z[r]= a[p]
                    r,p = r + 1, p + 1
                elif a[q] <= a[p]:
                    z[r]= a[q]
                    r,q = r + 1, q + 1

            while p != b:
                
                z[r] = a[p]
                r, p = r + 1 , p + 1
            while q!=c:
                
                z[r]= a[q]
                r,q= r+ 1 ,q + 1
            r = d
            while r!=c:
              
                a[r] = z[r]
                r = r + 1
            d,b,c= d +2*k, b + 2*k, min((c+2*k),N)
        k = k*2
    return z
for i in autores:
	
	print(i)

a = ArrayT(contador - 1)
b = ArrayT(contador - 1)
for i in range(contador-1):
	a[i] = autores[i]
for i in range(contador-1):
	b[i] = libros[i]	

autores1 = merge_sort(autores)
libros1 = merge_sort(libros)
g = ArrayT(contador-1)
h = ArrayT(contador-1)
for i in a:
	
	print(i)

for i in range(contador-1):
	for j in range(contador-1):
		if a[j]==autores1[i]:
			g[i]= autores1[i] + "	" + b[j] + "\n"
for i in g:
	print(i)
for i in range(contador-1):
	for j in range(contador-1):
		if b[j]==libros1[i]:
			h[i] = libros1[i] + "	" + a[j] + "\n"
for i in h:
	print(i)

archivo = open("salida.txt","w")

for linea in h:
	archivo.write(linea)
archivo.write("                                       " + "\n")
for linea in g:
	archivo.write(linea)
