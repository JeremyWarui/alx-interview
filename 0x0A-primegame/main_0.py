#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))  # Expected Output: "Maria"
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected Output: "Ben"
nums = [0] * 100
for i in range(100):
        nums[i] = i * i

        print("Winner: {}".format(isWinner(100, nums)))
