def stringMerge(w1,w2):
	out = ''
	l1 = len(w1)
	l2 = len(w2)

	if l1 >= l2:
		maxStr = l2
	else:
		maxStr = l1

	for i in range(maxStr):
		out = out + w1[i]
		out = out + w2[i]
	
	if l1 > maxStr:
		out = out + w1[maxStr:l1]
	
	if l2 > maxStr:
		out = out + w2[maxStr:l2]

	return out 

print(stringMerge('day','time'))