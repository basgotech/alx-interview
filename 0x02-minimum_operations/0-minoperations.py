#!/usr/bin/python3
"""Minimum Operations"""


def primeFactorization(x):
    """function takes an integer x and returns
    a list of its prime factors."""
    div = 2
    array = list()
    while (div <= x):
        if x % div == 0:
            array.append(div)
            x /= div
        else:
            div += 1

    return array


def minOperations(n):
    """If n is less than or equal to 1, it's impossible
    to achieve it with the given operations"""
    min = 0
    factors = [x for x in primeFactorization(n)]
    occurences = {item: factors.count(item) for item in factors}
    for k, v in occurences.items():
        min += k * v
    return min
