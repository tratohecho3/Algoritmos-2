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


def selection_sort(a,b):
    for i in range(0,b-1):
        min=i
        for j in range(i+1,b):
            if a[min] > a[j]:
                min=j
        aux=a[min]
        a[min]=a[i]
        a[i]=aux
    return a


def bubble_sort(a):
    for j in range(0,len(a)):

        for i in  range(0,len(a)-1):
            if a[i+1]<a[i]:
                a[i],a[i+1]=a[i+1],a[i]
    return a
        

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


a =insertion_sort(lista)
b =bubble_sort(lista)
c =selection_sort(lista,len(lista))

print("Utilizando el metodo de Insertion Sort")
for i in range(0,len(a)):
    print(a[i])
print("Utilizando el metodo de Bubble Sort")
for i in range(0,len(b)):
    print(b[i])
print("Utilizando el metodo de Selection Sort")
for i in range(0,len(c)):
    print(c[i])