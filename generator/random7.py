import random

def lottery():
    # return 7 random numbers between 1 and 10
    # range() creates and returns a sequence of numbers 0 to 7
    # this sequence is iterable
    for _ in range(7):
        yield random.randint(1, 10)

# yield next item in lottery() only when requested!
for rand in lottery():
    print(rand)
