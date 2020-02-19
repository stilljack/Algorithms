#!/usr/bin/python

import argparse


# Write a function `find_max_profit` that receives as input a
# list of stock prices. Your function should return the
# maximum profit that can be made from a single buy and sell.
# You must buy first before selling; no shorting is allowed here.

def find_max_profit(prices):
    current_min: int = prices[0]
    max_profit: int = prices[1] - current_min
    i = 1
    previous = []
    print(prices)
    while i < len(prices):
        current_profit = prices[i] - current_min
        print(f"current profit {current_profit}")
        if current_min == 0 or prices[i] < current_min:
            current_min = prices[i]
            print(f"{current_min} = current_Min")
        else:
            if current_profit > max_profit:
                max_profit = current_profit
                print(f"{max_profit} = max_profit")
        i += 1
    return max_profit



#
# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#     args = parser.parse_args()
#
#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
