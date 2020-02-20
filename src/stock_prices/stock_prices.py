#!/usr/bin/python

import argparse


# Write a function `find_max_profit` that receives as input a
# list of stock prices. Your function should return the
# maximum profit that can be made from a single buy and sell.
# You must buy first before selling; no shorting is allowed here.

def find_max_profit(prices):
    price_difference: int = prices[0]
    max_profit: int = prices[1] - price_difference
    currentItemInListOfPrices = 1
 #   previous = []
    print(f"initial values for {prices} \n min={price_difference} \n max_profit={max_profit}")
    while currentItemInListOfPrices < len(prices):
        current_profit = prices[currentItemInListOfPrices] - price_difference
        print(f"current profit {current_profit}")
        if price_difference == 0 or prices[currentItemInListOfPrices] < price_difference:
            price_difference = prices[currentItemInListOfPrices]
            print(f"{price_difference} = current_Min")
        else:
            if current_profit > max_profit:
                max_profit = current_profit
                print(f"{max_profit} = max_profit")
        currentItemInListOfPrices += 1
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
