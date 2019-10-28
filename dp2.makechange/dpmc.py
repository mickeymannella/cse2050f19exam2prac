def dpMakeChange(coinValueList, change):
    # Create a list to store the answers to the subproblems
    minCoins = [None]*(change + 1)

    # For each value from 0 to change, compute the min number of coins needed.
    for cents in range(change+1):
        # Assume at first that all 1's are used.
        minCoins[cents] = cents
        # Check if any coin leads to a better solution to our current best.
        for c in coinValueList:
            if cents >= c:
                minCoins[cents] = min(minCoins[cents], minCoins[cents - c] + 1)

    # Return just the element in the table corresponding to the desired value.
    return minCoins[change]

print(dpMakeChange([1,5,10,21,25], 63))
print(dpMakeChange([1,5,10,21,25], 64))