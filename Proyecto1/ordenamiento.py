
import math
from arrayT import ArrayT
from random import randint
#FUNCIONA 


def insertion_sort(a):
    for j in range(1,len(a)):

        llave = a[j]
        i = j-1
        while i >= 0 and a[i] > llave:
            a[i+1] = a[i]
            i =  i - 1
        a[i + 1] = llave

    return a

def partition(A,p,r,x):
	i = p 
	j = r - 1
	while True:
		if A[j] <= x:
			j = j - 1
		if A[i] >= x:
			i = i + 1
		if i < j:
			A[i], A[j] = A[j], A[i]
		else:
			return j


#FUNCIONA
def introsort(A):
	f = 0
	b = len(A)
	introsort_loop(A,f,b,2*math.log(b-f,2))
	insertion_sort(A)
	return A

#FUNCIONA
def introsort_loop(A,f,b,depth_limit):

	while b -f > 10:
		if depth_limit == 0:
			heap_sort(A)
			return A

		depth_limit = depth_limit - 1
		p = partition(A, f, b, Mediana(A[f], A[int(f+(b-f)/2)], A[b-1]))
		introsort_loop(A, p, b, depth_limit)
		b = p
	return A

#FUNCIONA
def quicksort(A):
	f = 0
	b = len(A)
	quicksort_loop(A,f,b)
	insertion_sort(A)
	return A
#FUNCIONA
def quicksort_loop(A,f,b):

	while b -f > 10:

		p = partition(A,f,b,Mediana(A[f],A[int(f + (b - f) / 2)],A[b -1]))
		if 	p -f >= b -p:
			quicksort_loop(A,p,b)
			b = p
		else:
			quicksort_loop(A,f,p)
			f = p


#FUNCIONA
def Mediana(a,b,c):
	medio = 0
	if a >= b and b >= c:
		medio = b
	elif a >= c and c >= b:
		medio = c
	elif b >= a and a >= c:
		medio = a
	elif b >= c and c >= a:
		medio = c
	elif c >= a and a >= b:
		medio = a
	elif c >= b and b >=a:
		medio = b
	return medio

#FUNCIONA
def Quicksort_Yaroslavskiy(A):
	left = 0
	right = len(A)-1
	Quicksort_Yaroslavskiy1(A,left,right)
	return A

def Quicksort_Yaroslavskiy1(A, left,right):
	M = len(A)
	if right - left < M:
		insertion_sort(A)
	else:
		if A[left]>A[right]:
			p,q = A[right], A[left]
		else:
			p,q = A[left], A[right]
		l,g,k = left + 1, right - 1, l
		while k <= g:
			if A[k]<p:
				A[k],A[l]=A[l],A[k]
				l = l+1
			else: 
				if A[k]>=q:
					while A[g]>q and k < g:
						g = g - 1
					if A[g]>=p:
						A[k],A[g]=A[g],A[k]
					else:
						A[k],A[g]=A[g],A[k]
						A[k],A[l]=A[l],A[k]
						l = l+1
					g = g - 1
			k = k + 1
		l,g = l-1,g+1
		A[left] = A[l]
		A[l]=p
		A[right] = A[g]
		A[g] = q
		Quicksort_Yaroslavskiy(A,left,l-1)
		Quicksort_Yaroslavskiy(A,l+1,g-1)
		Quicksort_Yaroslavskiy(A,g+1,right)
	return A					

#FUNCIONA
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

#FUNCIONA
def build_max_heap(array):
    i = len(array)//2
    while i >= 0:
        heapify(array,i,len(array))
        i = i -1
    return array
#FUNCIONA
def swap(array, i, j):
    array[i],array[j]=array[j],array[i]
    return array

#FUNCIONA    
def heap_sort(array):
    build_max_heap(array)
    i = len(array)-1
    while i >= 1:
        swap(array,0,i)
        heapify(array,0,i)
        i = i -1
    return array

#FUNCIONA
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
   


#FUNCIONA
def particion(A,p,r):
    x = A[r]
    i = p -1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1 
#FUNCIONA
def particion_randomizado(A,p,r):
    i = randint(p,r)
    A[r], A[i] = A[i], A[r]
    return particion(A,p,r)
#FUNCIONA
def quicksort_randomizado(A):
    p = 0
    r = len(A) - 1
    quicksort_randomizado_auxiliar(A,p,r)
    return A
#FUNCIONA
def quicksort_randomizado_auxiliar(A,p,r):
    if p < r:
        q = particion_randomizado(A,p,r)
        quicksort_randomizado_auxiliar(A,p,q-1)
        quicksort_randomizado_auxiliar(A,q+1,r)
    return A

#FUNCIONA
def parent(i):
    return ((i + 1) // 2) - 1
#FUNCIONA
def left(i):
    return (2*(i+1)-1)
#FUNCIONA
def right(i):
    return (2*(i+1))


#FUNCIONA

def Quicksort_3_partitioning(A):
	l = 0
	r = len(A)-1
	Quicksort_3_partitioning1(A,l,r)
	return A

def Quicksort_3_partitioning1(A,l,r):
	if r - l + 1 >= 10:
		i = l-1
		j=r
		p= l-1
		q=r
		if r <= l:
			return
		v=A[r]	 
		while True:
			i += 1
			while A[i]<v:
				i += 1
				if i == len(A):
					break
			j = j-1	
			while v < A[j]:
				if j == l:
					break
				j = j -1	
			if i >= j:
				break

			A[i],A[j] = A[j],A[i]


			if A[i]==v:
				p += 1
				A[p],A[i]=A[i],A[p]
			if v == A[j]:
				q = q - 1
				A[j],A[q] = A[q],A[j]
		A[i],A[r]=A[r],A[i]
		j = i-1
		i = i+1
		for k in range(l,p):
			A[k],A[j]=A[j],A[k]
			j = j - 1
		for k in range(r-1,q,-1):
			A[i],A[k]=A[k],A[i]
			i = i+1
		Quicksort_3_partitioning1(A,l,j)
		Quicksort_3_partitioning1(A,i,r)
	else:
		insertion_sort(A)
	return A