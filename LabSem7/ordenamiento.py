from arrayT import ArrayT
from prueba2 import counting_sort_auxiliar

def counting_sort(A):
	B = ArrayT(len(A))
	K = A[0]
	for i in range(len(A)):
		if A[i] >= K:
			K = A[i]
	counting_sort_auxiliar(A,B,K)
	return B
 