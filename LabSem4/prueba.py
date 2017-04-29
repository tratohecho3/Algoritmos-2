from arrayT import ArrayT

lista = [5,45,9,2,20,8,100,20,5,1,2,3,4]
def build_max_heap(array):
    i = len(array)//2
    while i >= 0:
        heapify(array,i,len(array))
        i = i -1
    return array

def swap(array, i, j):
    array[i],array[j]=array[j],array[i]
    return array

    
def heap_sort(array):
    build_max_heap(array)
    i = len(array)-1
    while i >= 1:
        swap(array,0,i)
        heapify(array,0,i)
        i = i -1
    return array

def heapify(array, i, lenght):

    Hijo_Izquierdo = left(i)
    Hijo_Derecho = right(i)
    el_mayor = i
    if Hijo_Izquierdo < lenght and array[Hijo_Izquierdo]>array[i]:
        el_mayor = Hijo_Izquierdo

    if Hijo_Derecho < lenght and array[Hijo_Derecho]>array[el_mayor]:
        el_mayor = Hijo_Derecho

    if el_mayor != i:
        swap(array,el_mayor,i)
        heapify(array,el_mayor,lenght)
    return array
   
def dequeue(array):
    if len(array) < 1:
        print(" El arreglo debe tener mas de un elemento")
    aux_array = arrayT(len(array)- 1)
    for i in range(0,len(array) - 2):
        aux_array[i] = array[i]

    heapify(aux_array,0,len(aux_array))
    return(array[0],aux_array)



def parent(i):
    return ((i + 1) // 2) - 1

def left(i):
    return (2*(i+1)-1)

def right(i):
    return (2*(i+1))

a = heap_sort(lista)
print(a)