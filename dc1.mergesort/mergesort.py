def mergeSort(L):
    if len(L) < 2:
        return

    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    mergeSort(A)
    mergeSort(B)
    merge(A, B, L)

def merge(A, B, L):
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i += 1
        else:
            L[i + j] = B[j]
            j += 1
    L[i + j:] = A[i:] + B[j:]

L = [5,2,3,1,4]
mergeSort(L)
print(L)