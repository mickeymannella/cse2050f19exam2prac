import sys

def fibmem(n):
    known = [0] * (n + 1)
    known[0] = 0
    known[1] = 1
    for i in range(2, n + 1):
        known[i] = known[i-1] + known[i-2]
    return known[n]

print(fibmem(int(sys.argv[1])))
