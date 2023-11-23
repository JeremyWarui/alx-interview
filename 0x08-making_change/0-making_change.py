#!/usr/bin/python3

"""makeChange problem"""


def makeChange(coins, total):
    """The function takes an array of coins
    returns total no of coins to meet the total

    Args: coins array and total no of coins

    Returns: no of coins to meet the total
    """
    if total <= 0:
        return 0

    next_coin = total + 1
    min_coins = {0: 0}

    for i in range(1, total + 1):
        min_coins[i] = next_coin
        for coin in coins:
            curr = i - coin
            if curr < 0:
                continue
            min_coins[i] = min(min_coins[curr] + 1, min_coins[i])
    if min_coins[total] == total + 1:
        return -1
    return min_coins[total]

    # if min_coins[total] != float('inf') or min_coins[total] == (total + 1):
    # return min_coins[total]
    # else:
    #     return -1
