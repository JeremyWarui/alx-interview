#!/usr/bin/python3

"""prime game"""


def isWinner(x, nums):
    """returns the winner"""
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # function to generate list of primes upto a limit
    def sieve(limit):
        # create a set of numbers from 2 to limit
        # numbers = set(range(2, limit + 1))
        # loop through each number checking if its prime
        # and remove its multiples from the set
        # for i in range(2, int(limit ** 0.5) + 1):
        #    if i in numbers:
        #        for j in range(i * 2, limit + 1, i):
        #            numbers.discard(j)
        numbers = list(range(2, limit + 1))
        for i in numbers:
            if is_prime(i):
                for j in range(i * 2, limit + 1, i):
                    if j in numbers:
                        numbers.remove(j)
        return numbers

    maria_wins = 0
    ben_wins = 0

    # loop through each round of the game
    for i in range(x):
        # get limit for the round
        limit = nums[i]
        # generate list of primes upto limit
        primes = sieve(limit)
        # set turns
        turn = "Maria"

        # loop until there are no primes left
        while primes:
            prime_max = max(primes)
            # remove the max prime num and its multiples
            # new_primes = [m for m in primes if m % prime_max != 0 or
            #              m == prime_max]
            primes.remove(prime_max)
            for q in primes:
                if q % prime_max == 0 or q == prime_max:
                    primes.remove(prime_max)
            # switch turns
            if turn == "Maria":
                turn = "Ben"
            else:
                turn = "Maria"
            # primes = new_primes
        # if maria's turn ended last, then ben wins
        if turn == "Maria":
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
