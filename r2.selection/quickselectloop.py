from random import randrange

def quickselect(L, k):
    left, right = 0, len(L)
    while left < right:
        pivot = partition(L, left, right)
        if k <= pivot:
            right = pivot
        elif k == pivot + 1:
            return L[pivot]
        else:
            left = pivot + 1
            return L[left]

def partition(L, left, right):
    pivot = randrange(left, right)
    L[pivot], L[right -1] = L[right -1], L[pivot]
    i, j, pivot = left, right - 2, right - 1
    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while i < j and L[j] >= L[pivot]:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    L[pivot], L[i] = L[i], L[pivot]    
    return i

print(quickselect([1,2,3,4,5], 4))