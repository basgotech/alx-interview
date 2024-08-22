#!/usr/bin/python3
"""
Making Change
"""

def minimumCoins(coin_values, target_amount):
    """
    Return the minimum number of coins needed to meet a given total.
    Args:
        coin_values (list of ints): a list of coins of different values
        target_amount (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if target_amount <= 0:
        return 0
    if coin_values == [] or coin_values is None:
        return -1
    try:
        coin_index = coin_values.index(target_amount)
        return 1
    except ValueError:
        pass

    coin_values.sort(reverse=True)
    total_coins = 0
    for coin in coin_values:
        if target_amount % coin == 0:
            total_coins += int(target_amount / coin)
            return total_coins
        if target_amount - coin >= 0:
            if int(target_amount / coin) > 1:
                total_coins += int(target_amount / coin)
                target_amount = target_amount % coin
            else:
                total_coins += 1
                target_amount -= coin
                if target_amount == 0:
                    break
    if target_amount > 0:
        return -1
    return total_coins
