#!/usr/bin/python3
"""Minimum Operations"""


def primeFactorization(x):
    """function takes an integer x and returns
    a list of its prime factors."""
    ispri = 2
    array_list = list()
    while (ispri <= x):
        if x % ispri == 0:
            array_list.append(ispri)
            x /= ispri
        else:
            ispri += 1

    return array_list


def minOperations(n):
    """If n is less than or equal to 1, it's impossible
    to achieve it with the given operations"""
    min_val = 0
    fac_val = [x for x in primeFactorization(n)]
    con = {item: fac_val.count(item) for item in fac_val}
    for a, b in con.items():
        min_val += a * b
    return min_val
