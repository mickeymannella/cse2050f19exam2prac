import sys

def fibmemo(n, known = dict()):
    if n == 0 or n == 1:
        known[n] = n
        return n
    elif n in known:
        return known[n]
    else:
        for i in range(2, n + 1):
            known[i] = fibmemo(i - 1, known) + fibmemo(i - 2, known)
        return known[n]

print(fibmemo(int(sys.argv[1])))
