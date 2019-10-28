from bufferediterator import BufferedIterator

def mergesort(L):
    if len(L) > 1:
        m = len(L) // 2
        A, B = L[:m], L[m:]
        mergesort(A)
        mergesort(B)
        L[:] = merge(A, B)

def merge(A, B):
    a = BufferedIterator(A)
    b = BufferedIterator(B)
    while a.hasnext() or b.hasnext():
        if not a.hasnext() or (b.hasnext() and b.peek() < a.peek()):
            yield next(b)
        else:
            yield next(a)