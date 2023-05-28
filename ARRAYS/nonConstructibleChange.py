#TIME COMPLEXITY O(nlogn)
#SPACE COMPLEXITY O(1)
def nonConstructibleChanges(coins):
    coins.sort()

    currentChangedCoins = 0
    for coin in coins:
        if coin > currentChangedCoins +1:
            return currentChangedCoins + 1
        currentChangedCoins += coin

    return currentChangedCoins + 1