"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autor: Cesar Colina 13-10299
         Ian Goldberg 14-10406
# email: tratohecho3@gmail.com 
         14-10406@usb.ve
"""
from arrayT import ArrayT
n = int(input("Ingrese la cantidad de elementos de la lista a ordenadar "))
lista = ArrayT(n)

for i in range(n):
    lista[i] = n - i 



def insertion_sort(a):
    for j in range(1,len(a)):

        llave = a[j]
        i = j-1
        while i >= 0 and a[i] > llave:
            a[i+1] = a[i]
            i =  i - 1
        a[i + 1] = llave

    return a


def selection_sort(a):
    for i in range(len(a)):
        smallest = i
        for j in range(i+1,len(a)):
        	if a[smallest]>a[j]:
        		smallest = j
        aux = a[i]
        a[i]=a[smallest]
       	a[smallest]=aux
    return a
        


def bubble_sort(a):
    for j in range(0,len(a)):

        for i in  range(0,len(a)-1):
            if a[i+1]<a[i]:
                a[i],a[i+1]=a[i+1],a[i]
    return a
def merge_sort(a):
    z = ArrayT(len(a))
    k = 1
    N = len(a)
    while k < N:
        
        d,b,c = 0, k, min(2*k,N)

        while b < N:
            p,q,r = d,b,d
            

            while p!=b and q!=c:
                
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



        

def bubble_sort_modificado(a):
    """
    Implementacion del algoritmo Bubble Sort (1) del libro 
    Programming: the derivation of algorithms de Kaldewaij.
    
    Parametros:
        a: Un arreglo a ordenar

    Efecto Secundario:
        El arreglo de entrada es ordenado en orden ascendente
    """
    N = len(a)
    n = 0
    b = False
    while (n != N) and (not b):
        k = N - 1
        b = True
        while k != n:
            if a[k-1] > a[k]:
                b = False
                a[k-1], a[k] = a[k], a[k-1]
            k -= 1
        n += 1

""" Explicacion de los resultados obtenidos:
    El algoritmo MergeSort es el mas eficiente debido a que en lugar de comparar todos los elementos entre si, lo que hace es separar la lista 
    de elementos en varias listas, y estas a su vez en otras listas, hasta llegar a tener listas de 1 elemento, las cuales ya estan ordenadas.
    Posteriormente compara los elementos de dichas listas, uniendolas a una nueva lista en el orden encontrado.
"""