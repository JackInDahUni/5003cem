# Define a function named stringMerge that takes two strings, w1 and w2, as input parameters
def stringMerge(w1,w2):
    # Initialize an empty string to store the merged string
    out = ''
    # Calculate the lengths of w1 and w2
    l1 = len(w1)
    l2 = len(w2)

    # Determine the length of the shorter string among w1 and w2
    if l1 >= l2:
        maxStr = l2
    else:
        maxStr = l1

    # Iterate through the characters of both strings up to the length of the shorter string
    for i in range(maxStr):
        # Append the ith character of w1 to the output string
        out = out + w1[i]
        # Append the ith character of w2 to the output string
        out = out + w2[i]
    
    # If the length of w1 is greater than the length of the shorter string, append the remaining characters of w1 to the output string
    if l1 > maxStr:
        out = out + w1[maxStr:l1]
    
    # If the length of w2 is greater than the length of the shorter string, append the remaining characters of w2 to the output string
    if l2 > maxStr:
        out = out + w2[maxStr:l2]

    # Return the merged string
    return out 

# Call the stringMerge function with arguments 'day' and 'time' and print the result
print(stringMerge('day','time'))
