"""
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autor: Cesar Colina 13-10299
         Ian Goldberg 14-10406
# email: tratohecho3@gmail.com 
         14-10406@usb.ve

"""
from arrayT import ArrayT
from heap_functions import heap_sort

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
