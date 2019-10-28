import random

def lottery():
    # return 7 random numbers between 1 and 10
    for i in range(7):
        yield random.randint(1, 10)

# yield next item in lottery() only when requested!
for rand in lottery():
    print(rand)
