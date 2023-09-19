#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))  # Expected Output: "Maria"
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected Output: "Ben"
print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]))) # expected "None"
print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8]))) # EXPECTED "None"
print("Winner: {}".format(isWinner(0, [0]))) # expected "Maria"
