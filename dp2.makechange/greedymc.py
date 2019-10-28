def greedyMC(coinvalueList, change):
    coinvalueList.sort()
    coinvalueList.reverse()
    numcoins = 0
    for c in coinvalueList:
        # Add in as many coins as possible of the next largest value.
        numcoins += change // c
        # Update the amount of change left to return.
        change = change % c
    return numcoins

print(greedyMC([1,5,10,25], 63))
print(greedyMC([1, 21, 25], 63))
print(greedyMC([1, 5, 21, 25], 63))