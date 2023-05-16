#!/usr/bin/python3
"""
a list to track the fewest number of coins needed for each total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    if min_coins[total] > total:
        return -1
    else:
        return min_coins[total]
