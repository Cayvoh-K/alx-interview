#!/usr/bin/python3

"""
module game of choosing Prime numbers
"""


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    def generate_primes(n):
        """Return list of prime numbers between 1 and n inclusive
           Args:
            n (int): upper boundary of range. lower boundary is always 1
        """
        primes = []
        is_prime = [True] * (n + 1)
        p = 2

        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)

        return primes

    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = generate_primes(n)
        remaining_numbers = set(range(1, n + 1))

        for _ in range(x):
            current_player = "Maria"
            while True:
                valid_primes = [p for p in primes if p in remaining_numbers]
                if not valid_primes:
                    break

                chosen_prime = max(valid_primes)
                remaining_numbers -= set(range(chosen_prime, n + 1, chosen_prime))
                current_player = "Maria" if current_player == "Ben" else "Ben"

            if current_player == "Maria":
                winners["Ben"] += 1
            else:
                winners["Maria"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Maria"] < winners["Ben"]:
        return "Ben"
    else:
        return None
