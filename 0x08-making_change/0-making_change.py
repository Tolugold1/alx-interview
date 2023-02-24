#!/usr/bin/python3
"""Function that returns fewest number of
that makes up the total coin.
"""


def makeChange(coins, total):
    """return fewest coin"""
    if total < 1:
        return 0
    needed_coin = 0
    coins.sort()
    coins.reverse()
    for i in coins:
        if total <= 0:
            break
        temp = total // i
        needed_coin += temp
        total -= temp * i
    if total != 0:
        return -1
    return needed_coin
