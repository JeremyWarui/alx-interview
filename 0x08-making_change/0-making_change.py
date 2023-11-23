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

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        times = total // coin
        num_coins += times
        total -= coin * times
    if total != 0:
        return -1
    return num_coins
