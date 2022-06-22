def checksub(A,B):
    
    # if length of A is less than B, return False
    
    if len(A)<len(B):
        return False
    
    i = 0   # current index in A
    j = 0   # current index in B
    
    # iterate through A
    
    while i<len(A):
        # if the element at indices are same, then increment j (match next element)
        if A[i] == B[j]:
            j += 1
            if j == len(B):   # all characters are matched
                break
        i += 1
    return j == len(B)


A = list(map(int,input("Array to check: ").split(",")))
B = list(map(int,input("Sequence to check if is subsequence of the array: ").split(",")))
print(checksub(A,B))

