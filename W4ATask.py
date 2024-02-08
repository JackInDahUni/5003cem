def selection_Sort(A):					# defines the selection sort with the argument list A
	for i in range(len(A)-1):			# i itterates through the list
		minn = i						# the minn variable is then assigned to i
		j = i+1							# the variable j is assigned to the value i + 1
		for j in range (i, len(A)):		# j itterates through the list starting from i
			if A[j] < A[minn]:			# if element j is less than element minn
				minn = j				# minn is equal to j
		A[i], A[minn] = A[minn], A[i]	# element i is swapped with element minn
	return A							# returns the sorted list

print(selection_Sort([11, 22, 14, 67, 2, 9]))