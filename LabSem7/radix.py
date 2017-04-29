def radix_sort(A,d):
	for i in range(len(A)):
		k = A[0]
		if A[i] >= k:
			k = A[i]
	for i in range(len(A)):
		if len(str(A[i]))<d:
			aux = d - len(str(A[i]))
			A[i] = str(A[i])
			A[i] = aux*"0" + A[i]
			A[i] = int(A[i])
		counting_sort_mod(A,k,d)
	return A

def counting_sort_mod(A,k,d):
	for i in range(d+1,1,-1):
		B = [1,1,1,1,1,1,1,1,1,1,1,1]
		C = []
		for i in range(k+1):
			C.append(0)
		for i in range(k+1):
			C[i] = 0
		for i in range (len(A)):
			C[(A[i]%(10**d))] = C[(A[i]%(10**d))] + 1
		for i in range(1,K+1):
			c[i] = c[i] + c[i-1]
		for j in range(1,k+1):
			B[C[(A[j]%(10**d))]-1] = A[j]
			C[(A[j]%10**d)] = C[(A[j]%10**d)] -1
		for k in range(len(A)):
			A[i]=B[i]
	return A

a = [3,5,63,2,5,7,78,3,2,5,7,2]

a = radix_sort(a,2)
print(a)


def radix_sort(A,d):
	for i in range(len(A)):
		k = A[0]
		if A[i] >= k:
			k = A[i]
	for i in range(len(A)):
		if len(str(A[i]))<d:
			aux = d - len(str(A[i]))
			A[i] = str(A[i])
			A[i] = aux*"0" + A[i]
			A[i] = int(A[i])
		counting_sort_mod(A,k,d)
	return A

def counting_sort_mod(A,k,d):
	for i in range(d+1,1,-1):
		B = ArrayT(len(A))
		C = ArrayT(k+1)
		for i in range(k+1):
			C[i] = 0
		for i in range (len(A)):
			C[(A[i]%(10**d))//10**d] = C[(A[i]%(10**d))//10**d] + 1
		for j in range(1,k+1):
			B[C[(A[j]%(10**d))//10**d]] = A[j]
			C[(A[j]%10**d)//10**d] = C[(A[j]%10**d)//10**d] -1
		for k in range(len(A)):
			A[i]=B[i]
	return A

