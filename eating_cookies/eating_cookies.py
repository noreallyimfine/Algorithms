#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    if not cache:
        cache = [0 for _ in range(n+1)]
    # base case - 0 cookies
    if n == 0:
        cache[0] = 1
        return cache[0]
    elif n == 1:
        cache[1] = 1
        return cache[1]
    # base case - 1 cookie
    elif n == 2:
        cache[2] = 2
        return cache[2]
    if cache[n] == 0:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies."
              .format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
