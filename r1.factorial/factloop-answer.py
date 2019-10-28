def factloop(n):
    # set up local variables
    factorial = 1
    k = 1
    # loop
    while k < n + 1:
        factorial *= k
        k += 1
    # return answer
    return factorial

print(factloop(0))
print(factloop(1))
print(factloop(2))
print(factloop(3))
print(factloop(4))
print(factloop(5))
