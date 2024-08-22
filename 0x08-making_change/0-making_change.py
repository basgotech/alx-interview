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
        g = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    total_count = 0
    for x in coins:
        if sum % x == 0:
            total_count += int(sum / x)
            return total_count
        if sum - x >= 0:
            if int(sum / x) > 1:
                total_count += int(sum / x)
                sum = sum % x
            else:
                total_count += 1
                sum -= x
                if sum == 0:
                    break
    if sum > 0:
        return -1
    return total_count
