#!/usr/bin/python3

""" makeChange - function that takes coins and total
    Args - coins: coins of different values
         - total: total no of coins needed to meet the total
    Returns: Fewest coins needed to meet total
    If total is 0 or less, returns 0
    If total cannot be met by any number of coins, return -1
"""
from typing import List


def makeChange(coins: List, total: int) -> int:
    if total <= 0:
        return 0
    coins_ls = [0] + [float("inf")] * total

    for coin in coins:
        for i in range(coin, total + 1):
            coins_ls[i] = min(coins_ls[i], coins_ls[i - coin] + 1)
    return coins_ls[total] if coins_ls[total] != float("inf") else -1
