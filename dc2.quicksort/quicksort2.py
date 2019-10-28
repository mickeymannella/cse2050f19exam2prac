def quicksort(L, left = 0, right = None):
    if right is None:
        right = len(L)

    if right - left > 1:    
        mid = partition(L, left, right)
        quicksort(L, left, mid)
        quicksort(L, mid+1, right)

def partition(L, left, right):
    pivot = right - 1
    i = left        
    j = pivot - 1   

    while i < j:
        while L[i] < L[pivot]:
            i = i + 1
        while i < j and L[j] >= L[pivot]:
            j = j - 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot

L = [5,2,3,1,4]
quicksort(L)
print(L)