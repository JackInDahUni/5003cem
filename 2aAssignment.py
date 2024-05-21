def mergeSort(sequence):
    if len(sequence) <= 1:
        return sequence

    mid = len(sequence) // 2
    left = mergeSort(sequence[:mid])
    right = mergeSort(sequence[mid:])

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sequence[k] = left[i]
            i += 1
        else:
            sequence[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        sequence[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        sequence[k] = right[j]
        j += 1
        k += 1

    return sequence

sequence = [1, 2, 3, 4, 2, 1, 2, 5, 67]
sortedSequence = mergeSort(sequence)
print("Sorted sequence: ", sortedSequence)
