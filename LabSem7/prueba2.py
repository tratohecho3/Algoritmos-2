from arrayT import ArrayT
def counting_sort_auxiliar(A,B,K):
	c = ArrayT(K+1)
	for i in range(K+1):
		c[i] = 0
	for j in range(len(A)):
		c[A[j]] = c[A[j]] + 1
	for i in range(1,K+1):
		c[i] = c[i] + c[i-1]
	j = len(A)-1
	while j >= 0:
		B[c[A[j]]-1] = A[j]
		c[A[j]] = c[A[j]] - 1
		j = j - 1
	return B

