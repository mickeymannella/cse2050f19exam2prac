def mergeSort(L):
    if len(L) < 2:
        return

    mid = len(L)
    A = [:mid]
    B = [mid:]

    mergesort(A)
    mergesort(B)

    merge(A, B, L)

def merge(A, B, L):
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j} = A[i]
            i += 1
        else:
            L[i + j] = B[j]
            j += 1
    L[i + j:] = A[i:] + B[j:]
