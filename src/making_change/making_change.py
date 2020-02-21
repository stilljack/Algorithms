#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]
bucket = {1:0,5:0,10:0,25:0,50:0}
answer = {"answer":0}
current_total=0


def making_change(amount,denominations,cache={0:1,1:1}):
    def changer_recursive():
        for entity in range():
            pass
    if amount < 0:
        return 0
    if amount not in cache:
        for type in denominations:
            changer_recursive(type)


    return answer[amount]

def helper_check(target):
    current_total=0
    current_total+=bucket[1]+\
                   (bucket[5]*5)+\
                   (bucket[10]*10)+\
                   (bucket[25]*25)+\
                   (bucket[50]*1)
    print(f"current_total {current_total}")
    if target%current_total == 0:
        print(f"answer increased by one for\n bucker = {bucket}")
        answer["answer"]+=1


def making_change(amount, denominations,cache={0:1,1:1}):
    if amount < 0:
        return 0
    if amount not in cache:
        for half_dollars in range(0,amount,50):
            for quarter in range(0,amount,25):
                for dimes in range(0,amount,10):
                    for nickles in range(0,amount,5):
                        for pennies in range(amount):
                            bucket[1]+=1
                            helper_check(amount)
                        bucket[5]+=1
                        helper_check(amount)
                    bucket[10]+=1
                    helper_check(amount)
                bucket[25]+=1
                helper_check(amount)
            bucket[50]+=1
            print(f"bucket={bucket}")
            helper_check(amount)
    return(answer["answer"])



print(making_change(20,denominations))


# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")
