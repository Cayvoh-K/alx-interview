#!/usr/bin/python3
"""
a list to track the fewest number of coins needed for each total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    min_coins = [sys.maxsize] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    if min_coins[total] == sys.maxsize:
        return -1
    else:
        return min_coins[total]
