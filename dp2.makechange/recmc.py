def recMC(coinValueList, change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

# print(recMC([1,5,10,25],63)) # Seriously don't even try to run this
print(recMC([1, 21, 25],63))
print(recMC([1, 5, 21, 25],63))