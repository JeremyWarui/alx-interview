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
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    if min_coins[total] != float('inf') or min_coins[total] == (total + 1):
        return min_coins[total]
    else:
        return -1
