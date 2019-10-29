# make a factorial function using a loop

def factloop(n):
    # set up local variables
    product = 1    

    # loop
    for x in range(1, n + 1):
        product *= x

    # return answer
    return product

print(factloop(0))
print(factloop(1))
print(factloop(2))
print(factloop(3))
print(factloop(4))