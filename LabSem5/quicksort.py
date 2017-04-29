from random import randint

a = [2,5,4,3,10,20,2,1]
b = [1,200,42,22,1000, 1002, 150]
def quicksort_auxiliar(A,p,r):
    if p<r:
        q = particion(A, p, r)
        quicksort_auxiliar(A,p,q-1)

        quicksort_auxiliar(A,q+1,r)
    return A

def quicksort_basico(A):
    p = 0
    r = len(A)-1
    quicksort_auxiliar(A,p,r)
    return A



def particion(A,p,r):
    x = A[r]
    i = p -1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1 

def particion_randomizado(A,p,r):
    i = randint(p,r)
    A[r], A[i] = A[i], A[r]
    return particion(A,p,r)

def quicksort_randomizado(A):
    p = 0
    r = len(A) - 1
    quicksort_randomizado_auxiliar(A,p,r)
    return A

def quicksort_randomizado_auxiliar(A,p,r):
    if p < r:
        q = particion_randomizado(A,p,r)
        quicksort_randomizado_auxiliar(A,p,q-1)
        quicksort_randomizado_auxiliar(A,q+1,r)
    return A


# La prueba numero 2 y 3 deben realizarse con arreglos de muchos menos elementos, ya que por su poca eficiencia con arreglos ordenados 
# de forma descendente  y arreglos de 0 y 1, su eficiencia seria n^2. Para el caso del arreglo descendiente la funcion de quicksort se 
# llama a si misma n veces, ya que en cada iteracion el pivote utilizado es el menor numero no arreglado. Haciendo un total de 
# casi n pivotes al finalizar el ordenamiento. Para el caso de 5000 elementos la funcion de quicksort se llama a si misma una vez por 
# cada elemento menos el ultimo. Para el caso del arreglo generado solo con ceros y unos ocurre que, como el pivote se compara con los
# elementos del arreglo menores o iguales a el, tomamos el peor de los casos en el que el arreglo consta de muchos elementos con valor
# 1, como hay muchos elementos que son iguales al pivote el algoritmo va a estar constantemente haciendo swap entre ellos.