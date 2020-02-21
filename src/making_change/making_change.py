#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]
bucket = {1: 0, 5: 0, 10: 0, 25: 0, 50: 0}
answer = {"answer": 0}
current_total = 0
cache = {0: 0, 1: 1}

#OK LETS TRY THE "RIGHT WAY TO DO IT"
#HOLY CRAP THATS A BETTER SOLTUION!
def making_change(total, denominations):
    r = [1] + [0] * total
    for k in denominations:
        for i in range(k, len(r)):
            r[i] += r[i - k]
    return r[total]

print(making_change(100, [50, 20, 10, 5, 1]))

# WHY THE HELL DOESN'T THIS WORK????
# def making_change(amount, denominations, cache={0: 1,1:1}):
#     if amount == 1:
#         return 1
#     if amount == 0:
#         return 1
#     else:
#         return rec_making_change(amount, denominations, cache)
#
#
# def rec_making_change(amount, denominations, cache):
#     if amount in cache:
#         return cache[amount]
#     elif amount < 0 or not denominations:
#         return 0
#
#     coin = denominations[-1]
#     return (cache[amount] = sum(
#         rec_making_change(amt, denominations[:-1], cache)
#         for amt in range(amount, -1, -coin)
#     ))





    #  print(f"cache {amount} recorded for {cache[amount]} ")


#  return cache[amount]
# this works:
# def rec_making_change(amount, denominations,cache={0:1}):
#     if amount in cache:
#         return cache[amount]
#     elif amount < 0 or not denominations:
#         return 0
#     else:
#         coin = denominations[-1]
#         return sum(
#             rec_making_change(amt, denominations[:-1],cache)
#             for amt in range(amount, -1, -coin)
#         )

print(making_change(12, [1, 5, 10, 25, 50]))


def _ugg(amount, denominations, cache={0: 1, 1: 1}):
    def changer_recursive(n, denominations):
        for entity in range(len(denominations), 0, -1):
            print(f"entity = {denominations[entity - 1]}")
            pass

    if amount < 0:
        return 0

    if amount not in cache:
        for i in range(len(denominations), 0, -1):
            print(denominations[i - 1])
            changer_recursive(i, denominations)

    answer[amount] = 0
    return answer[amount]


# print(making_change(20,denominations))

def helper_check(target):
    current_total = 0
    current_total += bucket[1] + \
                     (bucket[5] * 5) + \
                     (bucket[10] * 10) + \
                     (bucket[25] * 25) + \
                     (bucket[50] * 1)
    print(f"current_total {current_total}")
    if target % current_total == 0:
        print(f"answer increased by one for\n bucker = {bucket}")
        answer["answer"] += 1
    return answer["answer"]


def making_change_old(amount, denominations, cache={0: 1, 1: 1}):
    if amount < 0:
        return 0
    if amount not in cache:
        for half_dollars in range(0, amount, 50):
            for quarter in range(0, amount, 25):
                for dimes in range(0, amount, 10):
                    for nickles in range(0, amount, 5):
                        for pennies in range(amount):
                            bucket[1] += 1
                            helper_check(amount)
                        bucket[5] += 1
                        helper_check(amount)
                    bucket[10] += 1
                    helper_check(amount)
                bucket[25] += 1
                helper_check(amount)
            bucket[50] += 1
            print(f"bucket={bucket}")
            helper_check(amount)
        cache[amount] = current_total
    return answer["answer"]

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")
