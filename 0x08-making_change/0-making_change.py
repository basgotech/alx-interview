#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for x in coins:
        if total % x == 0:
            coin_count += int(total / x)
            return coin_count
        if total - x >= 0:
            if int(total / x) > 1:
                coin_count += int(total / x)
                total = total % x
            else:
                coin_count += 1
                total -= x
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
