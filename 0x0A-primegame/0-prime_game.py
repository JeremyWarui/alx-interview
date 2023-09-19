#!/usr/bin/python3

"""prime game"""


def isWinner(x, nums):
    """returns the winner"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 0:
            ben_wins += 1
        elif n % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Ben"
    elif maria_wins < ben_wins:
        return "Maria"
    else:
        return None
