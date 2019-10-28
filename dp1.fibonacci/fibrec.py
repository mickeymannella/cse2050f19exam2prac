import sys

# This is NOT linearly recursive. each recursive call makes more than one recusive call.
# so... exponential recursion
# bottom line: it's slow. 

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(int(sys.argv[1])))
