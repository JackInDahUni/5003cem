def selection_Sort(A):
	for i in range(len(A)-1):
		minn = i
		j = i+1
		for j in range (len(A)):
			if A[j] < A[minn]:
				minn = j
		swap(A,i,minn)
	return A

def swap(A,i,minn):
