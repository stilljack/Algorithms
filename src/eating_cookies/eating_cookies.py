#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
memo = {}

def eating_cookies(n, cache={}):
    res = 0
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif cache and cache[n]>0:
        return cache[n]
    else:
        res = eating_cookies(n-1,cache)  +eating_cookies(n-2,cache) +eating_cookies(n-3,cache)
        cache[n] = res
        return res

def cookie_memoize(f):
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

sauce =cookie_memoize(eating_cookies)
print(sauce(100))


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
